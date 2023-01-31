import json
import os
import shutil

import library_functions as lf
import unreal

import importlib

from settings import app_context

importlib.reload(lf)


class SequenceRenderer:
    PRESET_PREVIEW = '/Game/__STAGE-0__/photostudio-portrait-20230122/presets/preset-photostudio-portrait-20230122-2145-FDAA1x1_preview.preset-photostudio-portrait-20230122-2145-FDAA1x1_preview'
    PRESET_HD = '/Game/__STAGE-0__/photostudio-portrait-20230122/presets/preset-photostudio-portrait-20230125-0853-HDAA2x2.preset-photostudio-portrait-20230125-0853-HDAA2x2'

    def process_render_queue(self, final_callback, resolution_width=1920, resolution_height=1080, spatial_sample_count=16):

        def process_next():
            os.makedirs(app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR, exist_ok=True)
            os.makedirs(app_context.RENDER_PIPELINE_FRAMES_COMPLETED_DIR, exist_ok=True)

            file_names = os.listdir(app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR)
            print(file_names)
            if not file_names:
                final_callback()
                return

            file_name = file_names[0]
            from_file = f'{app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR}/{file_name}'
            to_file = f'{app_context.RENDER_PIPELINE_FRAMES_COMPLETED_DIR}/{file_name}'
            shutil.move(from_file, to_file)

            with open(to_file) as f:
                data = json.loads(f.read())



            print(f'Processing {to_file}')
            print(f' -- {data}')

            preset = data['preset']
            level = data['level']
            sequence_path = data['sequence_path']
            render_cut_id = data['render_cut_id']
            start_frame = data['start_frame']
            end_frame = data['end_frame']
            output_path = data['output_path']

            lf.level_load_level(level)
            scene_sequence = lf.sequencer_load_sequence(sequence_path)

            lf.sequencer_set_range_frames(scene_sequence, start_frame=start_frame, end_frame=end_frame)
            sequence_path = lf.get_asset_path(scene_sequence)
            lf.sequencer_save_sequence(sequence_path)
            lf.sequencer_refresh_current_level_sequence()

            print('\n' * 5)
            print('*************')
            print(f'    - Rendering cut {render_cut_id} {start_frame} {end_frame}')


            # scene_sequence_path = lf.get_asset_path(scene_sequence)
            lf.render_sequence_to_images_aa(
                level_path=level,
                sequence_path=sequence_path, #scene_sequence_path,
                output_dir=output_path,
                preset=SequenceRenderer.PRESET_PREVIEW,
                resolution_width=resolution_width,
                resolution_height=resolution_height,
                spatial_sample_count=spatial_sample_count
            )

        app_context.render_callback = process_next
        process_next()
