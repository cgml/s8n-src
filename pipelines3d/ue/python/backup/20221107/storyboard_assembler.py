import os
import json
#import numpy as np



class CameraShotStyle:

    def __init__(self, focal_length: int):
        self.focal_length = focal_length
        self.UE_CAMERA_SHOT_TYPES = \
            json.loads(
                open('C:/s8n/system/s8n-src/pipelines3d/ue/python/_config/camera_shot_types.json').read()
            )


    def solve(self, animation_data, animation_start_offset_frame, start_frame, end_frame, ue_shot_type: str):
        camera_conf = self.UE_CAMERA_SHOT_TYPES[f'focal_length_{self.focal_length}'][ue_shot_type]
        target_bone = camera_conf['bone']

        bone_targets = []

        for frame_idx in sorted([int(k) for k in animation_data]):
            if frame_idx < start_frame:
                continue
            if frame_idx > end_frame:
                break

            target_bone_data = animation_data[str(frame_idx)]["bones"][target_bone]
            bone_targets.append(target_bone_data["bone_location"] + target_bone_data["bone_rotation"])

        # TODO use bone information to position camera
        # np_bone_targets = np.array(bone_targets)
        x_sum = 0
        for target in bone_targets:
            x, y, z, roll, yaw, pitch = target
            x_sum += x
        x_avg = x_sum / len(bone_targets)

        steps = end_frame - start_frame
        result = []
        for frame_idx in range(start_frame, end_frame+1):
            x, y, z, roll, yaw, pitch = -camera_conf["distance"], x_avg, camera_conf["height"], 0, 0, 0
            result.append((frame_idx, x, y - steps + frame_idx - start_frame, z, roll, yaw, pitch))
        return result



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
        'C:/s8n/linux-cp/data/output/analysis/video/ariana_grande_v2/ariana_grande_shot_types.csv'

    DEFAULT_VIDEO_TEMPLATE_PATH = \
        'C:/s8n/linux-cp/data/output/analysis/video/ariana_grande_v2/ariana_grande_v2_template.json'

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
        self.camera_shot_style = CameraShotStyle(focal_length=focal_length)

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



compositor = StoryboardCompositor_StaticVideoTemplate()


