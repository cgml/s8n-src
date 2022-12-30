import unreal



# INITITALIZE SEQUENCE
level = get_current_level()
actor = get_player('Player1')
animation = get_animation('/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted')
sequence = get_create_sequence()

studio_a_location = (0, 0, 0)
studio_b_location = (1000, 0, 0)

camera_a = get_camera('CameraA')
camera_b = get_camera('CameraB')

clean_sequence(sequence)

set_world_offset(studio_a_location)

sequence_add_actor(actor)

FPS = 30
DURATION_SEC = 30
DURATION_FRAMES = FPS * DURATION_SEC
sequence_set_parameters(fps=30, start_frame=0, end_frame=DURATION_FRAMES)

# LOAD STORY CONFIGURATION.
# FOR EACH STORY BLOCK ACTOR / ANIMATION
BLOCK_START_FRAME=0
BLOCK_END_FRAME=60

## 1. Set animation & time dilation
sequence_add_animation(actor, animation, start_frame=BLOCK_START_FRAME, end_frame=BLOCK_END_FRAME)
time_dilation_points = [(BLOCK_START_FRAME, 1.0), (BLOCK_START_FRAME+10, 0.5), (BLOCK_START_FRAME+20, 1.0), (BLOCK_END_FRAME, 1.0)]
sequence_set_timedilation(points=time_dilation_points)

## 2. VFX
sequence_add_vfx(actor, animation, start_frame=0, end_frame=60)


# FOR EACH CAMERA CUT
## 1. Set camera & cuts
get_bone_positions(actor, start_frame=0, end_frame=60)

camera_set_shottype(camera=camera_a, actor=actor, bone='head')
camera_set_shottype(camera_a, shottype='head')

# V2
# class CameraMovesGenerator:
#     def generate_camera_positions(self, camera_move_style, frames):
#
# solve_camera_positions(actor, animation, animation_offset=camera_cut_start - animation_start, )
# sequence_position_camera(camera_a, )

sequence_camera_cuts(camera_a, start_frame=0, end_frame=60)

## 2. Set Postprocess VFX & transitions
# V2
# sequence_transition(camera_a, start_frame=0, end_frame=1, style='fadein')
# sequence_transition(camera_a, start_frame=1, end_frame=60, style='pixalation')

'''
{
    'actor'
}
'''