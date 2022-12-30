import unreal
import unreal as ue

from unreal import MovieSceneAudioTrack, LevelSequenceFactoryNew, MovieSceneSkeletalAnimationTrack, Character, SkeletalMesh, MovieScene3DTransformTrack, CineCameraActor, AnimSequence
import time
from unreal import FloatRange, FloatRangeBound, MovieSceneObjectBindingID


def create_asset(asset_path='', asset_class=None, asset_factory=None):
    # asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().\
    #     create_unique_asset_name(base_package_name=asset_path, suffix='')

    if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
        path = asset_path.rsplit('/', 1)[0]
        name = asset_path.rsplit('/', 1)[1]
        return unreal.AssetToolsHelpers.get_asset_tools().\
            create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
    return unreal.load_asset(asset_path)

def spawn_actor(model_name: str):
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class(model_name)
    actor_location = unreal.Vector(0, 0, 0)
    rotation_location = unreal.Rotator(0, 0, 0)
    return unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, rotation_location)


# create a new level sequence asset
# factory = LevelSequenceFactoryNew()
# seq = factory.factory_create_new('/Game/MovieMaster' + str(int(time.time())))

BASE_PATH = '/Game/S8n-Experimental/MainExample/'
seq = unreal.load_asset(f'{BASE_PATH}sequencer_script')

unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(seq)

seq.get_playback_range().set_start_seconds(0)
seq.get_playback_range().set_end_seconds(30)

camera_track = seq.add_master_track(unreal.MovieSceneCameraCutTrack)

current_world = unreal.EditorLevelLibrary.get_editor_world()

# # spawn a new character and modify it (post_edit_change will allow the editor/sequencer to be notified of actor updates)
# # character = world.actor_spawn(Character)
#
# actor_location = unreal.Vector(0.0,0.0,0.0)
# actor_rotation = unreal.Rotator(0.0,0.0,0.0)
#
# # character = unreal.EditorLevelLibrary.spawn_actor_from_class(Character, actor_location, actor_rotation)
# #
# # # notify modifications are about to happen...
# # mesh = unreal.load_object(SkeletalMesh, '/Game/Mannequin/Character/Mesh/SK_Mannequin.SK_Mannequin')
# # character.modify()
# # character.Mesh.SkeletalMesh = mesh
# # # finalize the actor
# # character.post_edit_change()
#

model_character = spawn_actor("/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ")
actor_track = seq.add_possessable(model_character)
anim = actor_track.add_track(MovieSceneSkeletalAnimationTrack)

anim_sequence = anim.add_section()
anim_sequence.set_range_seconds(1, 3)
run_animation = unreal.AnimSequence.cast(unreal.load_asset('/Game/s8n/animations/mixamo-y-retargeted/Running03_InPlace_O00_Retargeted1'))
anim_sequence.params.animation = run_animation # unreal.load_object(AnimSequence, '/Game/Mannequin/Animations/ThirdPersonRun.ThirdPersonRun')
anim_sequence.set_range_seconds(0, 30)
anim_sequence.set_row_index(0)

# TODO
# anim_sequence2 = anim.add_section()
# anim_sequence2.set_row_index(1)
# anim_sequence2.set_range_seconds(2, 5)
#
# anim_sequence3 = anim.add_section()
# anim_sequence3.set_row_index(1)
# anim_sequence3.params.slot_name = 'Hello'
# anim_sequence3.set_range_seconds(0, 30)

# add a transform track/section in one shot to the actor
# TRANSFORMATION
transform_section = actor_track.add_track(MovieScene3DTransformTrack).add_section()
transform_section.set_range_seconds(0, 50)

transform_channels = transform_section.get_all_channels()
print(transform_channels)
exit(0)
for idx in range(1,10):
    for idc in range(6):
        k = transform_channels[idc].add_key(unreal.FrameNumber(idx*10), idx*100)


#TODO transform.set_property_name_and_path('Location', unreal.Transform(unreal.Vector(0, 0, 22 * 100))) # nreal.Transform(unreal.Vector(0, 0, 22 * 100)

# add keyframes to the transform section (from 4.20 you can directly use teh reflection api, and the methods returns the frame numbers)
# TODO print(transform.sequencer_section_add_key(0, unreal.Transform(unreal.Vector(0, 0, 17 * 100))))
# print(transform.sequencer_section_add_key(1.1, unreal.Transform(unreal.Vector(0, 0, 22 * 100))))
# print(transform.sequencer_section_add_key(2.2, unreal.Transform(unreal.Vector(0, 0, 26 * 100))))
# print(transform.sequencer_section_add_key(3.3, unreal.Transform(unreal.Vector(0, 0, 30 * 100))))

# add camera cut track (can be only one)

# TODO FROM C:\s8n\system\src\pipelines\s8n-alpha\ue\python\camera.py

def populate_track(track, num_sections=1, section_length_seconds=1):
    result = []
    for i in range(num_sections):
        section = track.add_section()
        section.set_start_frame_seconds(i * section_length_seconds)
        section.set_end_frame_seconds(section_length_seconds)
        result.append(section)
    return result


def create_level_sequence_with_spawnable_camera(sequence):
    # Create a cine camera actor
    camera_actor = unreal.EditorLevelLibrary().spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector(0, 0, 0),
                                                                      unreal.Rotator(0, 0, 0))

    # Add a spawnable using that cine camera actor
    camera_binding = sequence.add_spawnable_from_instance(camera_actor)

    # Add a cine camera component binding using the component of the camera actor
    camera_component_binding = sequence.add_possessable(camera_actor.get_cine_camera_component())
    camera_component_binding.set_parent(camera_binding)

    camera_component_binding.set_display_name('renamed')

    # Add a focal length track and default it to 60
    focal_length_track = camera_component_binding.add_track(unreal.MovieSceneFloatTrack)
    focal_length_track.set_property_name_and_path('CurrentFocalLength', 'CurrentFocalLength')
    focal_length_section = focal_length_track.add_section()
    focal_length_section.set_start_frame_bounded(0)
    focal_length_section.set_end_frame_bounded(0)

    for channel in focal_length_section.find_channels_by_type(unreal.MovieSceneScriptingFloatChannel):
        channel.set_default(60.0)

    # Add a transform track
    camera_transform_track = camera_binding.add_track(unreal.MovieScene3DTransformTrack)
    sections = populate_track(sequence, camera_transform_track, 1, 5)


    return sequence


create_level_sequence_with_spawnable_camera(seq)

#
# cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
# # Make sure your camera label is the same as in fbx file
# cine_camera.set_actor_label('ShotCam')
#
# binding = seq.add_possessable(cine_camera)
# seq.add_possessable(cine_camera.get_cine_camera_component())
#
# camera_id = unreal.MovieSceneObjectBindingID()
# camera_id.set_editor_property('guid', binding.get_id())
# camera_cut_track = seq.add_master_track(unreal.MovieSceneCameraCutTrack)
# camera_section = camera_cut_track.add_section()
# camera_section.set_range(0.0, 100.0)
# camera_section.set_camera_binding_id(camera_id)



exit(0)

camera_cut_track = seq.sequencer_add_camera_cut_track()

# add two camera views
camera1 = camera_cut_track.sequencer_track_add_section()
camera2 = camera_cut_track.sequencer_track_add_section()

# spawn 2 cine cameras in the stage and posses them with the sequencer
cine_camera = world.actor_spawn(CineCameraActor)
camera_guid = seq.sequencer_add_actor(cine_camera)

cine_camera2 = world.actor_spawn(CineCameraActor)
camera2_guid = seq.sequencer_add_actor(cine_camera2)

# assign the two cameras to the camera cut sections (via binding id)

camera1.CameraBindingID = MovieSceneObjectBindingID(
    Guid=unreal.string_to_guid( camera_guid ), Space=unreal.EMovieSceneObjectBindingSpace.Local
)
camera2.CameraBindingID = MovieSceneObjectBindingID(
    Guid=unreal.string_to_guid( camera2_guid ), Space=unreal.EMovieSceneObjectBindingSpace.Local
)

# set cameras ranges
camera1.sequencer_set_section_range(3.5, 5)
camera2.sequencer_set_section_range(0.5, 17)

# notify the sequence editor that something heavily changed (True will focus to the sequence editor)
seq.sequencer_changed(True)


# Sequence: add_possessable / add_spawnable
#   - add_master_track()
#   - add_possessable: Possesable (Actor)
#       - add_section():
#

# tx_channel =  trans_section.get_channels()[0]
# tx_channel.add_key(time=unreal.FrameNumber(10), new_value=50.0)