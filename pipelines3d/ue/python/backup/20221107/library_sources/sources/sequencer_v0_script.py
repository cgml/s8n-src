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


# LOAD SEQUENCER
sequence_path = '/Game/S8n-Experimental/x-generated-seq/scene_0000.scene_0000'
body_anim_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'

seq = unreal.load_asset(sequence_path)

unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(seq)

seq.get_playback_range().set_start_seconds(0)
seq.get_playback_range().set_end_seconds(30)

current_world = unreal.EditorLevelLibrary.get_editor_world()

# ADD MODEL

model_character = spawn_actor('/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005')
actor_track = seq.add_possessable(model_character)
anim = actor_track.add_track(MovieSceneSkeletalAnimationTrack)

anim_sequence = anim.add_section()
anim_sequence.set_range_seconds(1, 3)
run_animation = unreal.AnimSequence.cast(unreal.load_asset('/Game/s8n/animations/mixamo-y-retargeted/Running03_InPlace_O00_Retargeted1'))
# unreal.load_object(AnimSequence, '/Game/Mannequin/Animations/ThirdPersonRun.ThirdPersonRun')
anim_sequence.params.animation = run_animation
anim_sequence.set_range_seconds(0, 30)
anim_sequence.set_row_index(0)


# ADD CAMERA

# Get the control rig asset
rig = unreal.load_asset("/Game/Animation/ControlRig/Mannequin_ControlRig")

# Get the rig class
rig_class = rig.get_control_rig_class()

# Using the level sequence and actor binding, we can either find or create a control rig track from the class
rig_track = unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track(current_world, seq, rig_class, actor_track)


def add_camera_section(level_sequence, camera_actor, s, e):

    camera_binding = level_sequence.add_possessable(camera_actor)


    camera_cut_track = level_sequence.add_master_track(unreal.MovieSceneCameraCutTrack)

    camera_id = unreal.MovieSceneObjectBindingID()
    camera_id.set_editor_property('guid', camera_binding.get_id())

    camera_section = camera_cut_track.add_section()
    camera_section.set_range(s, e)
    camera_section.set_camera_binding_id(camera_id)



    # Add a spawnable using that cine camera actor
    # TODO camera_binding = level_sequence.add_spawnable_from_instance(camera_actor)

    # Add a cine camera component binding using the component of the camera actor
    #                          level_sequence.add_possessable(camera_actor.get_cine_camera_component())
    camera_component_binding = level_sequence.add_possessable(camera_actor.get_cine_camera_component())
    camera_component_binding.set_parent(camera_binding)

    camera_component_binding.set_display_name('CurrentFocalLength')

    # Add a focal length track and default it to 60
    focal_length_track = camera_component_binding.add_track(unreal.MovieSceneFloatTrack)
    focal_length_track.set_property_name_and_path('CurrentFocalLength', 'CurrentFocalLength')
    focal_length_section = focal_length_track.add_section()
    focal_length_section.set_start_frame_bounded(s)
    focal_length_section.set_end_frame_bounded(e)

    for channel in focal_length_section.find_channels_by_type(unreal.MovieSceneScriptingFloatChannel):
        channel.set_default(60.0)

    # Add a transform track
    camera_transform_track = camera_binding.add_track(unreal.MovieScene3DTransformTrack)

    # camera_track.add_track(MovieScene3DTransformTrack)
    transform_section = camera_transform_track.add_section()
    transform_section.set_range(s, e)

    transform_channels = transform_section.get_all_channels()
    print("TRANSFORM CHANNELS = ", transform_channels)

    for idc in range(6):
        k = transform_channels[idc].add_key(unreal.FrameNumber(0), 0)

    for idx in range(s, e):
        for idc in range(6):
            k = transform_channels[idc].add_key(unreal.FrameNumber(idx), idx)

    return level_sequence

for idx in range(1, 2):
    cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))
    cine_camera.set_actor_label(f'ShotCam {idx}')
    add_camera_section(seq, cine_camera, idx*10, (idx+1)*10)



# Sequence: add_possessable / add_spawnable
#   - add_master_track()
#   - add_possessable: Possesable (Actor)
#       - add_section():
#

# tx_channel =  trans_section.get_channels()[0]
# tx_channel.add_key(time=unreal.FrameNumber(10), new_value=50.0)