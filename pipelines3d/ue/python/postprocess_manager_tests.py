import unittest

from postprocess_manager import PostprocessorManager
from settings import app_context
import moviepy
from moviepy.editor import *
import numpy as np

class PostprocessorManagerTests(unittest.TestCase):
    def test_create_audio2(self):
        import pydub
        from pydub.playback import play

        music_1 = pydub.AudioSegment.from_mp3(file="C:\\s8n\\linux-cp\\data\\output\\audio\\mp3\\fr60cut_alexberoza_artnow.mp3")
        # Decrease the volume by 10 dB
        new_wav_file = music_1 - 10

        # # Reducing volume by 5
        # silent_wav_file = wav_file - 5

        play(music_1)

        #  Playing original file
        play(music_1)

    def test_create_audio(self):
        # moviepy.editor.
        music_1 = AudioFileClip("C:/s8n/linux-cp/data/output/audio/voice-over-mp3/fr60cut_alexberoza_drive.mp3")
        audio_1 = AudioFileClip("C:/s8n/linux-cp/data/output/audio/voice-over-mp3/voice-over-1.mp3")
        audio_2 = AudioFileClip("C:/s8n/linux-cp/data/output/audio/voice-over-mp3/voice-over-2.mp3")
        mixed = CompositeAudioClip([music_1, audio_1.set_start(10), audio_2.set_start(1)])
        mixed = mixed.set_fps(25)
        def make_frame(t):
            return np.zeros((128, 128))

        clip = VideoClip(make_frame, duration=60)
        clip = clip.set_audio(mixed)
        clip.write_videofile(
            filename="C:/s8n/system/src/x-generated/ue/audio_generated/fr60cut_alexberoza_artnow-with-voice-over.mp4",
            fps=25,
            audio = True
        )

    def test_create_move_files_instructions(self):
        postprocessor_manager = PostprocessorManager()
        instructions = [
            {
                "scene": "experimental-01_sequence-0001",
                "start_frame": 10,
                "end_frame": 10,
                "direction": "forward"
            },
            {
                "scene": "experimental-01_sequence-0002",
                "start_frame": 1,
                "end_frame": 2,
                "direction": "forward"
            },
            {
                "scene": "experimental-01_sequence-0003",
                "start_frame": 1,
                "end_frame": 2,
                "direction": "backward"
            }
        ]
        files_instructions = postprocessor_manager.create_move_files_instructions(sequence_instructions=instructions)
        self.assertTrue(len(files_instructions) == 5)
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/sequences/experimental-01_sequence-0001/output.0010.jpeg", files_instructions[0][0])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/final/final.0000.jpeg", files_instructions[0][1])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/sequences/experimental-01_sequence-0002/output.0001.jpeg", files_instructions[1][0])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/final/final.0001.jpeg", files_instructions[1][1])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/sequences/experimental-01_sequence-0002/output.0002.jpeg", files_instructions[2][0])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/final/final.0002.jpeg", files_instructions[2][1])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/sequences/experimental-01_sequence-0003/output.0002.jpeg", files_instructions[3][0])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/final/final.0003.jpeg", files_instructions[3][1])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/sequences/experimental-01_sequence-0003/output.0001.jpeg", files_instructions[4][0])
        self.assertEqual(f"{app_context.RENDER_ROOT_DIR}/final/final.0004.jpeg", files_instructions[4][1])
