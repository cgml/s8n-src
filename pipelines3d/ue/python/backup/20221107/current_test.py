import postprocess_manager as ppm
import sequence_instructions_executor as sie
import sequence_renderer
import golden_data
import sequencer_instructions_builder as sib
import importlib

importlib.reload(sib)
importlib.reload(sie)
importlib.reload(ppm)
importlib.reload(golden_data)
importlib.reload(sequence_renderer)

from golden_data import GoldenData


def postprocessor():
    output_project_dir = "C:/s8n/system/src/x-generated/ue/music-video-20221028"
    print('Running postprocessing')
    postprocessor = ppm.PostprocessorManager()
    print('Arrange output process')
    postprocessor.arrange_video_frames(sequence_instructions=GoldenData.sequence_instructions)
    print('Arrange ffmpeg process')
    postprocessor.generate_audio(
        output_project_dir=output_project_dir,
        sequence_instructions=GoldenData.sequence_instructions)
    postprocessor.ffmpeg_process(
        output_project_dir=output_project_dir,
        sequence_instructions=GoldenData.sequence_instructions
    )


sequence_instructions_builder = sib.SequenceInstructionsBuilder()
sequence_instructions = sequence_instructions_builder.create_instructions(storyboard=golden_data.GoldenData.storyboard)

executor = sie.SequenceInstructionsExecutor()
executor.process_sequence_instructions(sequence_instructions=sequence_instructions)
renderer = sequence_renderer.SequenceRenderer()
renderer.process_render_queue(postprocessor)

# print('Running postprocessing')
# postprocessor = ppm.PostprocessorManager()
# print('Arrange ffmpeg process')
# postprocessor.ffmpeg_process(
#     output_project_dir="C:/s8n/system/src/x-generated/ue/music-video-20221028",
#     music_path="C:/s8n/linux-cp/data/output/audio/mp3/fr60cut_alexberoza_artnow.mp3"
# )

# exit(0)
# # working
# import unreal
# import os
#
# umap = '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01'
# level_sequence = '/Game/S8n-Experimental/x-generated-seq/scene_0000.scene_0000'
#
# outdir = "C:/s8n/system/src/x-generated/ue/tmp" #os.path.abspath(os.path.join(unreal.Paths().project_dir(), 'out'))
# # fps = 60
# # frame_count = 120
#
# #Get movie queue subsystem for editor.
# subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
# q = subsystem.get_queue()
# executor = unreal.MoviePipelinePIEExecutor()
#
# #Optional: empty queue first.
# for j in q.get_jobs():
#     q.delete_job(j)
#
# #Create new movie pipeline job
# job = q.allocate_new_job(unreal.load_class(None, "/Script/MovieRenderPipelineCore.MoviePipelineExecutorJob"))
# job.set_editor_property('map', unreal.SoftObjectPath(umap))
# job.set_editor_property('sequence', unreal.SoftObjectPath(level_sequence))
#
# c=job.get_configuration()
# render_pass_settings=c.find_or_add_setting_by_class(unreal.MoviePipelineDeferredPassBase)
# output_setting: unreal.MoviePipelineOutputSetting=c.find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)
# output_setting.output_directory=unreal.DirectoryPath(outdir)
# output_setting.output_resolution.x = 3840
# output_setting.output_resolution.y = 2160
# # png_setting=c.find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_PNG)
# jpg_setting=c.find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_JPG)
# aa_settings: unreal.MoviePipelineAntiAliasingSetting = c.find_or_add_setting_by_class(unreal.MoviePipelineAntiAliasingSetting)
# print(aa_settings)
# aa_settings.spatial_sample_count = 64
# aa_settings.temporal_sample_count = 1
# aa_settings.override_anti_aliasing = True
# aa_settings.anti_aliasing_method = unreal.AntiAliasingMethod.AAM_NONE
#
# error_callback=unreal.OnMoviePipelineExecutorErrored()
# def movie_error(pipeline_executor,pipeline_with_error,is_fatal,error_text):
#     print(pipeline_executor)
#     print(pipeline_with_error)
#     print(is_fatal)
#     print(error_text)
# error_callback.add_callable(movie_error)
# def movie_finished(pipeline_executor,success):
#     print(pipeline_executor)
#     print(success)
# finished_callback=unreal.OnMoviePipelineExecutorFinished()
# finished_callback.add_callable(movie_finished)
#
# executor = subsystem.render_queue_with_executor(unreal.MoviePipelinePIEExecutor)
# if executor:
#     executor.set_editor_property('on_executor_errored_delegate',error_callback)
#     executor.set_editor_property('on_executor_finished_delegate',finished_callback)
