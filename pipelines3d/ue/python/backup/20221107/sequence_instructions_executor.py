import logging
import os
import time
import threading
from typing import Dict
import datetime as dt
import unreal
import json
import library_functions as lf

import importlib

import settings

importlib.reload(lf)
importlib.reload(settings)
from settings import app_context



class SequenceInstructionsExecutor:
    OUTPUT_DIR = "C:/s8n/system/src/x-generated/ue/music-video-20221028/sequences"
    WORK_DIR = '/Game/S8n-Experimental/x-generated-seq/'

    # DATA_DIR = 'C:/s8n/system/src/pipelines/s8n-alpha/ue/python/_data/render_jobs'
    # QUEUE_DIR = f'{DATA_DIR}/queue'

    def process_sequence_instructions(self, sequence_instructions):
        for scene_data in sequence_instructions:
            scene_name = scene_data["scene"]

            # TODO ! set FPS
            fps = scene_data["fps"]


            level_path = scene_data["level_path"]
            level_configuration = scene_data["level_path"]
            print(f'Processing scene {scene_name}, level {level_path}')
            print(f' - Opening level {level_path}')
            level = self._open_level(level_path)
            print(f' - Configuring level {level_path}')
            self.configure_level(level, level_configuration)
            print(f' - Generating scene sequence {scene_name}')
            scene_sequence = self.generate_scene_sequence(scene_data)
            print(f' - Rendering cuts')

            for render_cut in scene_data["render_cuts"]:
                start_frame = render_cut['start_frame']
                end_frame = render_cut['end_frame']
                scene_sequence_path = lf.get_asset_path(scene_sequence)
                os.makedirs(app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR, exist_ok=True)
                rendering_task = {
                    'level': level_path,
                    'level_configuration': level_configuration,
                    'sequence_path': scene_sequence_path,
                    'start_frame': start_frame,
                    'end_frame': end_frame,
                    'output_path': f"{self.OUTPUT_DIR}/{scene_name}_{start_frame}_{end_frame}"

                }
                with open(f'{app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR}/{scene_name}_{start_frame}_{end_frame}.json', 'w') as f:
                    f.write(json.dumps(rendering_task))

    def generate_scene_sequence(self, scene_data):
        scene_name = scene_data['scene']
        total_scene_range = scene_data["total_scene_range"]
        print(f' - Deleting old sequence {scene_name}')
        self._delete_sequence(sequence_name=scene_name)
        print(f' - Creating new sequence {scene_name}')
        level_sequence = self._create_sequence(sequence_name=scene_name, start_frame=total_scene_range[0], end_frame=total_scene_range[1])
        print(f' - New sequence created {level_sequence}')
        print(f' - Saving sequence {level_sequence}')
        self._save_sequence(level_sequence)
        print(f' - Open sequence {level_sequence}')
        self._open_sequence(level_sequence)
        print(f' - Refresh current sequence')
        self._save_sequence(level_sequence)
        for player_data in scene_data['players']:
            self._add_player(level_sequence, player_data)
        for mesh_data in scene_data['meshes']:
            self._add_mesh(level_sequence, mesh_data)
        self._add_camera(level_sequence, camera_data=scene_data['camera_shots'])

        total_scene_range_start = scene_data['total_scene_range'][0]
        total_scene_range_end = scene_data['total_scene_range'][1]
        fps=scene_data['fps']
        self._set_sequence_range(level_sequence,start_frame=total_scene_range_start, end_frame=total_scene_range_end, fps=fps)
        self._refresh_current_sequence()
        return level_sequence

    def _delete_sequence(self, sequence_name):
        lf.sequencer_delete_sequence(f"{self.WORK_DIR}/{sequence_name}")

    def _create_sequence(self, sequence_name, start_frame, end_frame):
        level_sequence = lf.sequencer_create_level_sequence(self.WORK_DIR, sequence_name)
        lf.sequencer_set_range_frames(level_sequence, start_frame=start_frame, end_frame=end_frame)
        return level_sequence

    def _open_sequence(self, level_sequence):
        lf.editor_open_level_sequence(level_sequence)

    def _save_sequence(self, level_sequence):
        sequence_path = lf.get_asset_path(level_sequence)
        lf.sequencer_save_sequence(sequence_path)

    def _refresh_current_sequence(self):
        lf.sequencer_refresh_current_level_sequence()

    def _add_player(self, sequence, player_data):
        player_name = player_data['name']
        player = self._get_player(label=player_name)
        # TODO! spawn player in level and then cleanup!
        print(f' - Found player {player}')
        player_track = self._add_player_track(sequence, player)
        self._add_face_animations(sequence=sequence, player=player, face_animations_data=player_data['face_animations'])
        self._add_body_animations(sequence=sequence, player=player, body_animations_data=player_data['body_animations'])

    def _get_player(self, label):
        player = lf.level_get_actor_by_label(label)
        return player

    def _add_player_track(self, sequence, player):
        print(f' - Create player track for {player} in sequence {sequence}')
        player_track = lf.sequence_add_player_track(sequence=sequence, player=player)
        return player_track

    def _add_face_animations(self, sequence, player, face_animations_data):
        print(f' - Creating face animation track for {player}')
        face_track = self._add_face_binding_track(sequence=sequence, player=player)
        for animation_idx, face_animation in enumerate(face_animations_data):
            face_animation_path = face_animation['ue_path']
            start_frame = face_animation['start_frame']
            end_frame = face_animation['end_frame']
            offset = face_animation['offset']   # TODO ! Use animation offset
            print(f'    - Creating face animation for {face_track} {face_animation_path}: {start_frame}-{end_frame} ')
            section = lf.sequencer_add_animation_to_animation_track(
                anim_track=face_track,
                animation_path=face_animation_path,
                range_start_frame=start_frame,
                range_end_frame=end_frame,
                row_index=animation_idx)

    def _add_face_binding_track(self, sequence, player):
        return lf.add_face_binding_track(level_sequence=sequence, actor=player)

    def _add_body_animations(self, sequence, player, body_animations_data):
        print(f' - Creating body animation track for {player}')
        body_track = lf.add_body_binding_track(level_sequence=sequence, actor=player)
        for animation_idx, body_animation in enumerate(body_animations_data):
            body_animation_path = body_animation['ue_path']
            start_frame = body_animation['start_frame']
            end_frame = body_animation['end_frame']
            offset = body_animation['offset']   # TODO ! Use animation offset
            print(f'   - Creating body animation for {body_track} {body_animation_path} {start_frame} {end_frame}')
            lf.sequencer_add_animation_to_animation_track(
                body_track,
                body_animation_path,
                start_frame,
                end_frame,
                offset
            )

    def _add_mesh(self, sequence, mesh_data):
        pass

    def _add_camera(self, sequence, camera_data):
        # print(lf.level_spawn_camera('CameraA'))
        cine_camera = lf.level_get_actor_by_label('CameraA')
        # lf.sequencer_create_camera_cut(level_sequence=sequence, cine_camera=cine_camera, start_frame=0,
        #                                end_frame=260, camera_section_data={}, focal_length=5)
        # return
        for camera_section_idx, camera_section_data in enumerate(camera_data):
            start_frame = camera_section_data["start_frame"]
            end_frame = camera_section_data["end_frame"]
            lf.sequencer_create_camera_cut(
                level_sequence=sequence,
                cine_camera=cine_camera,
                start_frame=start_frame,
                end_frame=end_frame,
                camera_section_data=camera_section_data
            )

    def _set_sequence_range(self, scene_sequence, start_frame, end_frame, fps):
        lf.sequencer_set_range_frames(scene_sequence, start_frame=start_frame, end_frame=end_frame)
        lf.sequencer_set_working_range(scene_sequence, start_sec=start_frame/fps-1, end_sec=end_frame/fps+1)
        self._save_sequence(scene_sequence)

    def _render_scene_sequence(self, scene_sequence, output_path):
        scene_sequence_path = lf.get_asset_path(scene_sequence)
        lf.render_sequence_to_images(scene_sequence_path, output_path)

    def _open_level(self, level_path):
        #########################################
        # OPEN LEVEL
        editor_world = lf.level_get_editor_world()
        if level_path not in str(editor_world):
            lf.level_load_level_experimental()
            editor_world = lf.level_get_editor_world()
        return editor_world

    def configure_level(self, level, level_configuration):
        for property in level_configuration:
            # TODO set level properties and execute blueprints
            pass


