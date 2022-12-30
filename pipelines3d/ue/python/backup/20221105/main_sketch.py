import unreal
import json
import library_functions as lf

import importlib
importlib.reload(lf)


#########################################
# OPEN LEVEL
editor_world = lf.level_get_editor_world()
if '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01' not in str(editor_world):
    lf.level_load_level_experimental()
    editor_world = lf.level_get_editor_world()

# TODO lf.level_spawn_elisa_character_to_current_level()

#########################################
# EXPORT / LOAD ANIMATION DATA
model_character = lf.level_get_actor_by_label('PlayerA')
animation_name = 'Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'
anim_sequence_path = f'/Game/s8n/animations/mixamo-y-retargeted/{animation_name}'

# - solve camera

animation_data = json.loads(open(f'C:/s8n/system/src/x-exported/s8n-alpha/ue/_exported_animation/{animation_name}.json').read())
camera_focal_length = 50
camera_distance_start = 100

#########################################
# OPEN SEQUENCER
sequence_path = '/Game/S8n-Experimental/MainExample/mhbones_getpos.mhbones_getpos'
sequence = lf.sequencer_load_sequence(sequence_path)
lf.editor_open_level_sequence(sequence)

#########################################
# ADD MODEL & SET ANIMATION
print(model_character)
lf.sequencer_add_animation_track(
    sequence=sequence,
    model_character=model_character,
    animation_path=anim_sequence_path, range_start=0, range_end=250, row_index=0)


#######################################
# ADD CAMERA CUTS AND CAMERA ANIMATION

# print(lf.level_spawn_camera('CameraA'))
cine_camera=lf.level_get_actor_by_label('CameraA')
print(f"CAMERA A={cine_camera}")


lf.sequencer_create_camera_cut(level_sequence=sequence, cine_camera=cine_camera, start_frame=0, end_frame=260, camera_section_data={}, focal_length=5)
if False:
    lf.sequencer_create_camera_cut(level_sequence=sequence, cine_camera=cine_camera, start_frame=-10, end_frame=50, camera_section_data={}, focal_length = 5)
    lf.sequencer_create_camera_cut(level_sequence=sequence, cine_camera=cine_camera, start_frame=50, end_frame=150, camera_section_data={}, focal_length = 5)
    lf.sequencer_create_camera_cut(level_sequence=sequence, cine_camera=cine_camera, start_frame=150, end_frame=260, camera_section_data={}, focal_length = 5)

lf.sequencer_set_range_frames(sequence, 0, 260)
lf.sequencer_refresh_current_level_sequence()

# lf.rendering_render_sequence_to_movie_minimal(sequence_path)
