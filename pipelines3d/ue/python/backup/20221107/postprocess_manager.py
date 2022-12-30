import os
import shutil
from typing import List, Dict, Tuple

from settings import app_context
import datetime as dt

class PostprocessorManager:

    def create_move_files_instructions(self, sequence_instructions: List[Dict]) -> List[Tuple[str, str]]:
        result = []
        current_final_frame = 0
        for instruction in sequence_instructions:
            scene = instruction['scene']
            for render_cut in instruction['tracks']['video']:
                frame_start = render_cut['start_frame']
                frame_end = render_cut['end_frame']
                direction = render_cut.get('direction', 'forward')
                if direction == 'forward':
                    frames = range(frame_start, frame_end)
                elif direction == 'backward':
                    frames = range(frame_start, frame_end)[::-1]
                else:
                    raise NotImplementedError(f'direction {direction} not supported')
                scene_render_cut = f"{scene}_{frame_start}_{frame_end}"     #_{direction}
                for frame_idx in frames:
                    source = os.path.join(app_context.RENDER_SEQUENCES_DIR, scene_render_cut, f'output.{frame_idx:04d}.jpeg').replace('\\', '/')
                    destination = os.path.join(app_context.RENDER_FINAL_DIR, f'final.{current_final_frame:04d}.jpeg').replace('\\', '/')
                    result.append((source, destination))
                    current_final_frame += 1
                    print(source, destination)
        return result

    def arrange_video_frames(self, sequence_instructions: List[Dict]):
        move_files_instructions = self.create_move_files_instructions(sequence_instructions)
        for instruction in move_files_instructions:
            print(instruction)
            shutil.copyfile(instruction[0], instruction[1])

    def generate_audio(self, output_project_dir, sequence_instructions):
        music_path = sequence_instructions['tracks']['music']
        # TODO Movie.py combine tracks
        os.makedirs(f'{output_project_dir}/final_audio', exist_ok=True)
        audio_path = f'{output_project_dir}/final_audio/audio.mp4'
        shutil.copyfile(music_path, audio_path)


    def ffmpeg_process(self, output_project_dir, sequence_instructions) -> str:
        date_str = dt.datetime.now().strftime('%Y-%m-%d-%H-%M')
        ffmpeg_c = "C:/s8n/system/tools/ffmpeg/bin/ffmpeg.exe"
        output_path = f"{output_project_dir}/final_mp4/video-{date_str}.mp4"
        command = f"{ffmpeg_c} -r 24 -f image2 -s 1920x1080 -i {output_project_dir}/final/final.%04d.jpeg -vcodec libx264 -crf 1 {output_path}".replace('/','\\')
        print(f'Running: {command}')
        result = os.system(command)
        print(result)
        final_output_path = f"{output_path}_a.mp4"
        audio_path = f'{output_project_dir}/final_audio/audio.mp4'
        command_audio = f"{ffmpeg_c} -i {output_path} -i {audio_path} -map 0:v -map 1:a -c:v copy -shortest {final_output_path}".replace('/','\\')
        print(f'Running: {command_audio}')
        result = os.system(command_audio)
        print(result)
        return final_output_path

    def color_correction_process(self, output_video_path):
        # TODO color correction profile
        print('not implemented')

