import json

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

