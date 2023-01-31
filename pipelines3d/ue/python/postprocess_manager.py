import logging
import os
import shutil
import glob
from typing import List, Dict, Tuple

from settings import app_context
import datetime as dt

class PostprocessorManager:

    def create_move_files_instructions(self, sequence_instructions: Dict, format: str = 'png') -> List[Tuple[str, str]]:
        result = []
        current_final_frame = 0
        # for instruction in sequence_instructions['tracks']['video']:

        for render_cut in sequence_instructions['tracks']['video']:
            scene = render_cut['scene']
            render_cut_id = render_cut['render_cut_id']
            frame_start = render_cut['start_frame']
            frame_end = render_cut['end_frame']
            expected_frames = render_cut['expected_frames']
            direction = render_cut.get('direction', 'forward')
            frames = range(frame_start, frame_end)
            scene_render_cut = f"{scene}_{render_cut_id}"     #_{direction} _{frame_start}_{frame_end}
            source_file_paths = []
            for frame_idx in frames:
                # source_path_template = os.path.join(app_context.RENDER_SEQUENCES_DIR, scene_render_cut, f'output.{frame_idx:04d}.*.{format}') #.replace('\\', '/')
                source_path_template = os.path.join(app_context.RENDER_SEQUENCES_DIR, scene_render_cut, f'output.{frame_idx:04d}.*.{format}').replace('\\', '/')
                print(f'Adding files to copy by template {source_path_template}')
                for source_file_path in glob.glob(rf'{source_path_template}'):
                    destination_file_path = os.path.join(app_context.RENDER_FINAL_DIR, f'final.{current_final_frame:04d}.{format}') #.replace('\\', '/')
                    print(f'Adding path to copy {source_file_path}')
                    # shutil.copy(file, destination_file_path)
                    source_file_paths.append(source_file_path) #, destination_file_path))
                    # current_final_frame += 1

            # Use only expected frames number:
            # In current implementation system doesn't know what's time dilation was used
            # In order to be precise in the number of frames taken from slow motion clips expected_frames is used
            source_file_paths = source_file_paths[-expected_frames:]
            if direction == 'forward':
                pass
            elif direction == 'backward':
                source_file_paths = source_file_paths[::-1]
            else:
                raise NotImplementedError(f'direction {direction} not supported')



            for source_file_path in source_file_paths:
                # source_path_template = os.path.join(app_context.RENDER_SEQUENCES_DIR, scene_render_cut, f'output.{frame_idx:04d}.*.{format}') #.replace('\\', '/')
                destination_file_path = os.path.join(app_context.RENDER_FINAL_DIR, f'final.{current_final_frame:04d}.{format}') #.replace('\\', '/')
                print(f'Adding files to copy by template {source_file_path} to {destination_file_path}')
                result.append((source_file_path, destination_file_path))
                current_final_frame += 1

        return result

    def arrange_video_frames(self, sequence_instructions: Dict):
        move_files_instructions = self.create_move_files_instructions(sequence_instructions)
        for instruction in move_files_instructions:
            print(f"Executing file copy: {instruction[0]} -> {instruction[1]}")
            os.makedirs(os.path.dirname(instruction[1]), exist_ok=True)
            shutil.copyfile(instruction[0], instruction[1])

    def generate_audio(self, output_project_dir, sequence_instructions):
        music_path = sequence_instructions['tracks']['audio']['music']['file_path']
        # TODO Movie.py combine tracks
        os.makedirs(f'{output_project_dir}/final_audio', exist_ok=True)
        audio_path = f'{output_project_dir}/final_audio/audio.mp4'
        shutil.copyfile(music_path, audio_path)

    # TODO resolution=1920x1080
    def ffmpeg_process(self, output_project_dir, sequence_instructions, format: str = 'png', fps: str = '30', resolution: str='640x480') -> str:
        print("THAT IS NEW ********************")

        date_str = dt.datetime.now().strftime('%Y-%m-%d-%H-%M')
        ffmpeg_c = "C:/s8n/system/tools/ffmpeg/bin/ffmpeg.exe"
        final_mp4_dir = f"{output_project_dir}/final_mp4"
        os.makedirs(final_mp4_dir, exist_ok=True)
        output_path = f"{final_mp4_dir}/video-{date_str}.mp4"
        if format == 'png':
            command = f"{ffmpeg_c} -r 24 -f image2 -s {resolution} -i " \
                      f"{output_project_dir}/final/final.%04d.{format} -pix_fmt yuv420p -vcodec libx264 -crf 10 {output_path}".replace('/',
                                                                                                                 '\\')

        else:
            command = f"{ffmpeg_c} -r 24 -f image2 -s {resolution} -i " \
                      f"{output_project_dir}/final/final.%04d.{format} -vcodec libx264 -crf 10 {output_path}".replace('/', '\\')

        # command = f"{ffmpeg_c} -r {fps} -f image2 -s {resolution} -i {output_project_dir}/final/final.%04d.{format} -vcodec libx264 -crf 1 {output_path}".replace('/','\\')
        logging.info(f'Running: {command}')
        print(f'Running: {command}')
        result = os.system(command)
        logging.info(result)
        print(result)
        final_output_path = f"{output_path}_a.mp4"
        audio_path = f'{output_project_dir}/final_audio/audio.mp4'
        command_audio = f"{ffmpeg_c} -i {output_path} -i {audio_path} -map 0:v -map 1:a -c:v copy -shortest {final_output_path}".replace('/','\\')
        logging.info(f'Running: {command_audio}')
        print(f'Running: {command_audio}')
        result = os.system(command_audio)
        logging.info(result)
        return final_output_path

    def color_correction_process(self, output_video_path):
        # TODO color correction profile
        print('not implemented')

