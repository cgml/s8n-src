import unreal
import library_functions as lf

import importlib
importlib.reload(lf)

face_animation_path = '/Game/s8n/animations/livelink/photostudio-hq/2022-09-04/Face_Archetype_Skeleton_Sequence.Face_Archetype_Skeleton_Sequence'
body_anim_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'

level_path = "/Game/s8n/scenes/experimental-01/experimental-01.experimental-01"
model_ue_path = "/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ"


level = lf.level_load_level_experimental()

sequence_path = '/Game/S8n-Experimental/x-generated-seq/scene_0000.scene_0000'

lf.sequencer_delete_sequence(sequence_path)
lf.sequencer_create_level_sequence('/Game/S8n-Experimental/x-generated-seq/', 'scene_0000')
level_sequence = lf.sequencer_load_sequence(sequence_path)

lf.editor_open_level_sequence(level_sequence)

# actor_system = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# Get the selected actor
# IT WORKS ONLY IF ACTOR SELECTED IN UNREAL ENGINE!
# actor_system.get_selected_level_actors()[0]

actor = lf.level_get_actor_by_label("PlayerA")

body_track = lf.add_body_binding_track(level_sequence, actor)
face_track = lf.add_face_binding_track(level_sequence, actor)
lf.sequencer_add_animation_to_animation_track(
    body_track,
    body_anim_sequence_path,
    0,
    100,
    0
)
lf.sequencer_add_animation_to_animation_track(
    face_track,
    face_animation_path,
    0,
    100,
    0
)

lf.sequencer_set_range_frames(level_sequence, 0, 300)
fps = 30
lf.sequencer_set_working_range(level_sequence, -2, 300/fps+2)
# print(level_sequence.set_playback_range(0,600))
lf.sequencer_refresh_current_level_sequence()

level_sequence_path = lf.get_asset_path(level_sequence)

lf.render_sequence_to_images(level_sequence_path, "C:/s8n/system/src/x-generated/ue/tmp")