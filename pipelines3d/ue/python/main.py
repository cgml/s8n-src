import logging

from gameplay_manager import gameplay_manager
from music_manager import music_manager
import storyboard_assembler as sa
import json


import postprocess_manager as ppm
import sequence_instructions_executor as sie
import sequence_renderer
import golden_data
import unreal
import sequencer_instructions_builder as sib
import importlib

importlib.reload(sib)
importlib.reload(sie)
importlib.reload(ppm)
importlib.reload(golden_data)
importlib.reload(sequence_renderer)




class S8nMainMovieManager:
    def execute(self, gameplays, music, video_style, duration=None, workdir_path = None):
        # 0. Generate gameplay in UE from GPT-3 story

        # 1. Load gameplay
        gameplay = gameplay_manager.load_gameplay()

        # 2. Select music
        music_analysis = music_manager.load_music_analysis()
        music_path = music_manager.get_music_path()
        # 3. Select style <=
        assembler = sa.StoryboardAssembler_StaticVideoTemplate(
            video_template_path=sa.StoryboardAssembler_StaticVideoTemplate.DEFAULT_VIDEO_TEMPLATE_PATH
        )

        # 4. Generate storyboard
        storyboard = assembler.create_storyboard(gameplay, music_analysis)

        # 5. Create instructions
        sequence_instructions_builder = sib.SequenceInstructionsBuilder()
        sequence_instructions = sequence_instructions_builder.create_instructions(storyboard=golden_data.GoldenData.storyboard)

        # 5. Build sequences for rendering
        sequence_instructions_executor = sie.SequenceInstructionsExecutor()
        sequence_instructions_executor.process_sequence_instructions(sequence_instructions=sequence_instructions)

        def run_postprocessors():
            # 7. Combine image frames into video
            print('Running postprocessing')
            postprocessor = ppm.PostprocessorManager()
            print('Arrange output process')
            postprocessor.arrange_video_frames(sequence_instructions=sequence_instructions)
            print('Arrange ffmpeg process')
            output_video_path = postprocessor.ffmpeg_process(
                output_project_dir="C:/s8n/system/src/x-generated/ue/music-video-20221028",
                sequence_instructions=sequence_instructions
            )
            logging.info(f'Generate video: {output_video_path}')

        renderer = sequence_renderer.SequenceRenderer()
        renderer.process_render_queue(final_callback=run_postprocessors)



s8n_main_movie_manager = S8nMainMovieManager()
s8n_main_movie_manager.execute(gameplays=['TODO'], music='TODO', video_style='TODO')

# if __name__ == '__main__':
#     # TODO ARGPARSE
#     pass
