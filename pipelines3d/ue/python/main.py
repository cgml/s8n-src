import logging
import datetime as dt
import os
import shutil
import sys

if sum([1 for v in sys.path if 's8n-src' in v]) == 0:
    print('Adding path: C:/s8n/system/s8n-src/pipelines3d/ue/python')
    sys.path.append('C:/s8n/system/s8n-src/pipelines3d/ue/python')

from gameplay_manager import gameplay_manager
import music_manager
import storyboard_assembler as sa
import json


import postprocess_manager as ppm
import sequence_instructions_executor_simple as sie
import sequence_renderer
import golden_data
import unreal
import sequencer_instructions_builder as sib
import importlib

from settings import app_context

importlib.reload(sa)
importlib.reload(sib)
importlib.reload(sie)
importlib.reload(ppm)
importlib.reload(golden_data)
importlib.reload(sequence_renderer)
importlib.reload(music_manager)

import logging



class S8nMainMovieManager:
    def execute(self, gameplays, music, video_style, duration=None, workdir_path = None):
        if False:
            # 0. Generate gameplay in UE from GPT-3 story

            # 1. Load gameplay
            gameplay = gameplay_manager.load_gameplay()

            # 2. Select music
            music_analysis = music_manager.music_manager.load_music_analysis()
            music_path = music_manager.music_manager.get_music_path()
            # 3. Select style <=
            assembler = sa.StoryboardAssembler_StaticVideoTemplate(
                video_template_path=sa.StoryboardAssembler_StaticVideoTemplate.DEFAULT_VIDEO_TEMPLATE_PATH
            )

            # 4. Generate storyboard
            storyboard = assembler.create_storyboard(gameplay, music_analysis)

        # 2. Cleanup previous
        if os.path.exists(app_context.RENDER_ROOT_DIR):
            os.makedirs(f'{app_context.RENDER_ROOT_DIR}_rendered', exist_ok=True)
            source_dir = app_context.RENDER_ROOT_DIR
            dest_dir = f"{app_context.RENDER_ROOT_DIR}_rendered/{os.path.basename(app_context.RENDER_ROOT_DIR)}_{dt.datetime.now().strftime('%Y-%m-%d-%H-%M')}"
            print(f'Found existing rendered dir. Moving from {source_dir} to {dest_dir}')
            shutil.move( source_dir, dest_dir)


        # 5. Create instructions
        sequence_instructions_builder = sib.SequenceInstructionsBuilder()
        sequence_instructions = sequence_instructions_builder.create_instructions(storyboard=golden_data.GoldenData.storyboard)

        # 5. Build sequences for rendering - Generate rendering instructions
        sequence_instructions_executor = sie.SequenceInstructionsExecutor()
        sequence_instructions_executor.process_sequence_instructions(sequence_instructions=sequence_instructions)


        def run_postprocessors():
            # 7. Combine image frames into video
            logging.info('Running postprocessing')
            postprocessor = ppm.PostprocessorManager()
            logging.info('Arrange output process')
            postprocessor.arrange_video_frames(sequence_instructions=sequence_instructions)
            logging.info('Arrange ffmpeg process')
            postprocessor.generate_audio(
                output_project_dir=app_context.RENDER_ROOT_DIR,
                sequence_instructions=sequence_instructions)


            output_video_path = postprocessor.ffmpeg_process(
                output_project_dir=app_context.RENDER_ROOT_DIR, #"C:/s8n/system/src/x-generated/ue/music-video-20221028",
                sequence_instructions=sequence_instructions
            )
            logging.info(f'Generate video: {output_video_path}')

        if True:
            renderer = sequence_renderer.SequenceRenderer()
            renderer.process_render_queue(final_callback=run_postprocessors)
        else:
            run_postprocessors()

s8n_main_movie_manager = S8nMainMovieManager()
s8n_main_movie_manager.execute(gameplays=['TODO'], music='TODO', video_style='TODO')
