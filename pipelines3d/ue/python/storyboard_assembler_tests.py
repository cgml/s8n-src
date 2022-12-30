import unittest
import json
import numpy as np

import storyboard_assembler as sa
from golden_data import GoldenData


class StoryboardAssemblerTests(unittest.TestCase):
    def test_create_storyboard(self):
        assembler = sa.StoryboardAssembler_StaticVideoTemplate()
        music_analysis_path = 'C:/s8n/linux-cp/data/output/analysis/audio/v3_s8n/fr60cut_alexberoza_artnow.mp3.json'
        music_analysis = json.loads(open(music_analysis_path).read())

        storyboard = assembler.create_storyboard(gameplay=GoldenData.gameplay, music_analysis=music_analysis)
        {
            "scenes":{
                "0000_scene":{

                }
            },
            "audio":{

            },
            "meta": {

            },
        }
        print(storyboard)

class CameraSolverTests(unittest.TestCase):

    def process_sections_to_sec(self, sections, min_section_sec: int = 1, max_section_sec: int = 3):
        processed_sections = []
        current_section_start = None
        current_section_end = None
        current_peaks = False
        current_valleys = False
        avg_energy = []

        for section in sections:
            if current_section_start is None:
                current_section_start = section[0]
                current_peaks = False
                current_valleys = False
            avg_energy.append(section[4])
            current_peaks = current_peaks or section[2]
            current_valleys = current_valleys or section[3]
            current_section_end = section[1]
            if current_section_end - current_section_start < min_section_sec:
                continue

            # TODO pass beat info and change on beat
            boost = False
            time_dilation = 1.0
            if current_valleys and not current_peaks:
                time_dilation = 0.25
            elif not current_valleys and current_peaks:
                time_dilation = 1.0
                boost = True
            elif np.average(np.array(avg_energy)) < 0.6:
                time_dilation = 0.5
            elif np.average(np.array(avg_energy)) < 0.8:
                time_dilation = 1.0
            elif np.average(np.array(avg_energy)) > 1.0:
                time_dilation = 1.0
                boost = True

            if max_section_sec < current_section_end - current_section_start:
                processed_sections.append([current_section_start, current_section_start+max_section_sec, time_dilation, boost, current_peaks, current_valleys, np.array(avg_energy)])
                current_section_start = current_section_start+max_section_sec
            else:
                processed_sections.append([current_section_start, current_section_start+max_section_sec, time_dilation, boost, current_peaks, current_valleys, np.array(avg_energy)])
                current_section_start = None

            current_peaks = False
            current_valleys = False
            avg_energy = []

        return processed_sections

    def get_frame(self, sec, fps, time_dilation):
        '''
        UE time dilation mechanism keeps nominal frames but actual frames are increased due to time change
        E.g. 24th frame will represent 1 sec with time dilation 1, and 2 sec with time dilation 0.5
        '''
        return int(sec * fps * time_dilation)

    def process_sections_to_frames(self, sections_sec, fps: int = 24):
        result_sections = []
        for section in sections_sec:
            if result_sections:
                start_frame = result_sections[-1][1] + 1
            else:
                start_frame = 0

            start_sec, end_sec, time_dilation, boost, peak, valley, avg_energy = section
            time_dilation = 1.0 # TODO OVERRIDE FOR NOW UNTIL IMPLEMENT TIME_DILATION USAGE IN UE
            end_frame = start_frame + self.get_frame(end_sec - start_sec, fps, time_dilation)
            result_sections.append([start_frame, end_frame, time_dilation, boost])
        return result_sections

    def test_solve_camera_positions(self):


        animation_sequence = []
        animation_name = 'Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'
        animation_data = json.loads(
            open(f'C:/s8n/system/src/x-exported/s8n-alpha/ue/_exported_animation/{animation_name}.json').read())

        music_analysis_path = 'C:/s8n/linux-cp/data/output/analysis/audio/v3_s8n/fr60cut_alexberoza_artnow.mp3.json'
        music_analysis = json.loads(open(music_analysis_path).read())
        animation_sequence.append((0, 5, animation_name, animation_data, 10))
        animation_sequence.append((6, 25, animation_name, animation_data, 20))
        animation_sequence.append((26, 50, animation_name, animation_data, 40))

        sections = []
        for section_idx in sorted([int(k) for k in music_analysis["data"]]):
            section_data = music_analysis["data"][str(section_idx)]
            section_start_time = section_data['start_time']
            section_end_time = section_data['end_time']
            contains_energy_peak = section_data['contains_energy_peak']
            contains_energy_valley = section_data['contains_energy_valley']
            avg_chroma_energy = section_data['avg_chroma_energy']
              #   "beat_avg_energy": 0.5657342076301575,
              # "beat_energy_level_category": "high",
              # "beat_energy_peak": false,
              # "beat_energy_valley": false,
              # "beat_energy_impulses": []
            sections.append([section_start_time, section_end_time, contains_energy_peak, contains_energy_valley, avg_chroma_energy])

        sections_sec = self.process_sections_to_sec(sections)
        sections_frames = self.process_sections_to_frames(sections_sec=sections_sec)

        compositor = StoryboardCompositor_StaticVideoTemplate()


        for idx, section in enumerate(sections_frames):
            compositor.solve_camera_sections()
            camera_positions = compositor.solve(animation_data=animation_data, animation_start_offset_frame=0, start_frame=start_frame, end_frame=end_frame, ue_shot_type=shot_type)
            storyboard['camera_cuts'][str(start_frame)] = \
                {
                    "section_idx": idx,
                    "start_frame": start_frame,
                    "end_frame": end_frame,
                    "time_dilation": time_dilation,
                    "boost": boost,
                    "camera_positions": camera_positions,
                }


        for scene_section in composer_sections:
            start_frame = scene_section['start_frame']
            end_frame = scene_section['end_frame']
            frame_count = (end_frame - start_frame)
            self.assertTrue(24 <= frame_count <= 24 * 3)
            self.assertTrue(frame_count + 1 == len(scene_section['camera_positions']))



        for sequence in storyboard['sequences']:
            pass

        # Specify animations - story
        # Create animations per each location (= each location will have separate sequence)
        # Load animation data
        # Load music analysis
        # Use music analysis to generate section_frames (StoryboardAssembler):
        # For each section (Time - start/stop/time dilation, Energy info)
        #   - Use template to select
        #       - Shot Types
        #       - Camera Style from Shot type and Energy
        #       - Location
        #   - using Camera Shot Style, and animation data generate camera parameters
        #   - add camera cuts
        # Use animations to determine

        # Spawn actors with animations in specified levels / locations / scenes
