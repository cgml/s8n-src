import os
import json
import importlib

import camera_shots
importlib.reload(camera_shots)


class StoryboardAssembler_StaticVideoTemplate:
    '''
    Get music analysis

    '''
    MIN_SCENE_SEC = 1
    MAX_SCENE_SEC = 3

    UE_SHOT_TYPES = {
        "extra_long_shot": ["XLS", "XWS", "CI", "CA"],
        "long_shot": ["WS", "LS"],
        "full_shot": ["FS"],
        "medium_wide_shot": ["MWS", "MFS"],
        "cowboy_shot": ["COWS"],
        "medium_shot": ["MS"],
        "medium_close_up": ["MCS"],
        "close_up": ["CU", "WCU"],
        "extreme_close_up": ["XCU", "MCU"]
    }

    # TODO that is simplified hardcoded suequence path
    DEFAULT_SHOT_TYPE_SEQ_PATH = \
        'C:/s8n/system-linux/data/output/analysis/video/ariana_grande_v2/ariana_grande_shot_types.csv'

    DEFAULT_VIDEO_TEMPLATE_PATH = \
        'C:/s8n/system-linux/data/output/analysis/video/ariana_grande_v2/ariana_grande_v2_template.json'

    VIDEO_TEMPLATE = []

    def __init__(self, video_template_path=DEFAULT_VIDEO_TEMPLATE_PATH, focal_length=500):
        # TODO currently not used - refactor
        with open(video_template_path) as f:
            self.video_template = json.loads(f.read())

        self.US_SHOT_TYPES_REV = {}
        for k, val in self.UE_SHOT_TYPES.items():
            for v in val:
                self.US_SHOT_TYPES_REV[v] = k
        self.load_shot_type_sequence()
        self.camera_shot_style = camera_shots.CameraShotStyle(focal_length=focal_length)

    def load_shot_type_sequence(self, shot_type_seq_path: str = None):
        self.VIDEO_TEMPLATE = []
        if shot_type_seq_path is None:
            shot_type_seq_path = self.DEFAULT_SHOT_TYPE_SEQ_PATH

        for l in open(shot_type_seq_path).readlines():
            shot_type = l.split(',')[2]
            self.VIDEO_TEMPLATE.append(self.US_SHOT_TYPES_REV[shot_type])

    def get_camera_shot_style(self, section_idx, section):
        start_frame, end_frame, time_dilation, boost = section

        return self.VIDEO_TEMPLATE[section_idx % len(self.VIDEO_TEMPLATE)]

    def solve_camera(self, animation: dict, video_template: dict, music_analysis: dict):
        pass

    def create_storyboard(self, gameplay, music_analysis):
        pass




