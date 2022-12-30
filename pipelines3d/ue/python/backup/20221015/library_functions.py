from typing import Dict, Tuple, List

import unreal


##################################
##### LEVEL

def level_load_level(level_path: str):
    '''
    Load and open level
    '''
    world = unreal.EditorLoadingAndSavingUtils.load_map(level_path)
    return world

def level_load_level_experimental():
    return level_load_level('/Game/s8n/scenes/experimental-01/experimental-01.experimental-01')

def level_get_editor_world():
    '''
    Returns current editor world
    '''
    return unreal.EditorLevelLibrary.get_editor_world()


def level_spawn_camera(camera_name: str,
                       actor_location: unreal.Vector = unreal.Vector(0.0,0.0,0.0),
                       actor_rotation: unreal.Vector = unreal.Rotator(0.0,0.0,0.0)):
    cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
    cine_camera.set_actor_label(camera_name)
    return cine_camera

def level_set_camera_manual_focus(camera_object, manual_focus_distance: float, focus_offset: float):
    _focusSettings = unreal.CameraFocusSettings()
    _focusSettings.manual_focus_distance = manual_focus_distance
    _focusSettings.focus_method = unreal.CameraFocusMethod.MANUAL
    _focusSettings.focus_offset = focus_offset
    _focusSettings.smooth_focus_changes = False
    _cineCameraComponent = camera_object.get_cine_camera_component()
    _cineCameraComponent.set_editor_property("focus_settings", _focusSettings)


def level_set_camera_focus_method(camera_object, focus_method: float):
    """
    unreal.CameraFocusMethod.MANUAL
    """
    _focusSettings = unreal.CameraFocusSettings()
    _focusSettings.focus_method = focus_method
    _focusSettings.smooth_focus_changes = False
    _cineCameraComponent = camera_object.get_cine_camera_component()
    _cineCameraComponent.set_editor_property("focus_settings", _focusSettings)


def level_get_camera(camera_name: str):
    level_editor = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    camera_object = unreal.find_object(level_editor.get_current_level(), camera_name)
    return camera_object


def level_find_object(object_name: str):
    obj = unreal.find_object(level_get_editor_world(), name=object_name)
    return obj


def level_spawn_actor(model_name: str):
    '''
    Adds specified model by `model_name` to the current level
    Example:
        model_name = "/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ"
        level_spawn_actor(model_name)
    '''
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class(model_name)
    actor_location = unreal.Vector(0, 0, 0)
    rotation_location = unreal.Rotator(0, 0, 0)
    result = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, rotation_location)
    return result


def level_spawn_elisa_character_to_current_level():
    '''
    Spawn Elisa character to current level
    '''
    model_name = '/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005.BP_elisa-001-f1-005'
    return level_spawn_actor(model_name=model_name)


def level_get_actor_by_label(label):
    actor_system = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    for item in actor_system.get_all_level_actors():
        if label == item.get_actor_label():
            return item
    return None



##################################
##### SEQUENCER
def sequencer_load_sequence(sequence_path):
    sequence = unreal.load_asset(sequence_path, unreal.LevelSequence)
    return sequence


def sequencer_set_range(sequence, start_sec, end_sec):
    sequence.get_playback_range().set_start_seconds(start_sec)
    sequence.get_playback_range().set_end_seconds(end_sec)


def sequencer_create_camera_cut_hardcoded(
        level_sequence, cine_camera, start_frame: int, end_frame: int,
        camera_properties: Dict[str, List[Tuple[int, float]]],
        camera_transforms: [int, Tuple[float, float, float, float, float, float]]
):
    '''
    camera_properties
    - property name (e.g. CurrentFocalLength)
    - list of tuples [frame, value]
    '''
    ## 1. CAMERA CUTS SETUP
    # create camera binding to level sequence
    camera_binding = level_sequence.add_possessable(cine_camera)

    # create camera id
    camera_id = unreal.MovieSceneObjectBindingID()
    camera_id.set_editor_property('guid', camera_binding.get_id())

    # create camera cut track and assign camera by id to it
    camera_cut_track = level_sequence.add_master_track(unreal.MovieSceneCameraCutTrack)
    camera_section = camera_cut_track.add_section()
    camera_section.set_range(start_frame, end_frame)
    camera_section.set_camera_binding_id(camera_id)

    ## 2. FOCAL LENGTH SETUP
    # create camera component binding
    camera_component_binding = level_sequence.add_possessable(cine_camera.get_cine_camera_component())
    camera_component_binding.set_parent(camera_binding)

    camera_component_binding.set_display_name('CurrentFocalLength')

    # Add a focal length track and default it to 50
    focal_length_track = camera_component_binding.add_track(unreal.MovieSceneFloatTrack)
    focal_length_track.set_property_name_and_path('CurrentFocalLength', 'CurrentFocalLength')
    focal_length_section = focal_length_track.add_section()
    focal_length_section.set_start_frame_bounded(start_frame)
    focal_length_section.set_end_frame_bounded(end_frame)
    for channel in focal_length_section.find_channels_by_type(unreal.MovieSceneScriptingFloatChannel):
        print(f'For camera cut with start {start_frame} end {end_frame} frames. scripting float channel {channel}')
        channel.set_default(50.0)
        channel.add_key(unreal.FrameNumber(start_frame), 2)
        channel.add_key(unreal.FrameNumber(end_frame), 10)

    # 3. TRANSFORM TRACK SETUP
    # Add a transform track
    camera_transform_track = camera_binding.add_track(unreal.MovieScene3DTransformTrack)

    # camera_track.add_track(MovieScene3DTransformTrack)
    transform_section = camera_transform_track.add_section()
    transform_section.set_range(start_frame, end_frame)

    transform_channels = transform_section.get_all_channels()
    # print("TRANSFORM CHANNELS = ", transform_channels)

    # TODO PROVIDE TRANSITION PARAMETERS!
    if True:
        for idx in range(start_frame, end_frame):
            for idc in range(6):
                k = transform_channels[idc].add_key(unreal.FrameNumber(idx), idx)

def camera_transition(level_sequence, camera_actor, s, e):

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


def sequencer_create_level_sequence(sequence_path, sequence_name):
    level_sequence = unreal.LevelSequence.cast(unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=sequence_name,
        package_path=sequence_path,
        asset_class=unreal.LevelSequence,
        factory=unreal.LevelSequenceFactoryNew()
    ))
    return level_sequence


def sequencer_refresh_current_level_sequence():
    '''
    Refresh to visually see the new binding added
    '''
    unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence()

def sequencer_add_animation_track(sequence, model_character, animation_path: str, range_start, range_end, row_index):
    """
        -
        - animation_path - e.g.
            '/Game/s8n/animations/mixamo-y-retargeted/Running03_InPlace_O00_Retargeted1'
            run_animation = unreal.AnimSequence.cast(unreal.load_asset(animation_path))

    """
    actor_track = sequence.add_possessable(model_character)
    anim = actor_track.add_track(unreal.MovieSceneSkeletalAnimationTrack)

    anim_sequence = anim.add_section()
    anim_sequence.set_range(range_start, range_end)
    # anim_sequence.set_range_seconds(range_start, range_end)
    run_animation = unreal.AnimSequence.cast(unreal.load_asset(animation_path))
    anim_sequence.params.animation = run_animation
    anim_sequence.set_row_index(row_index)


##################################
##### EDITOR
def editor_open_level_sequence(sequence):
    unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(sequence)




##################################
##### RENDERING


def rendering_render_sequence_to_movie_minimal(sequencer_asset_path):
    '''
    Draft rendering of the sequence to AVI
    '''
    # If you do not override all of the settings in the AutomatedLevelSequenceCapture then the other settings are inherited
    # from Unreal's Class Default Object (CDO). Previous versions of Unreal (4.19 and below) stored the Render to Movie UI's settings in config files. Config
    # values are automatically loaded and applied to the CDO when the editor starts up. Unreal 4.20 and above now store the UI settings in a unique
    # instance in the config files, so modifications to the Render to Movie UI will no longer affect the CDO. However, legacy projects that are upgrading
    # from 4.19 to 4.20 may end up with the CDO being modified by their last Render to Movie UI settings. The CDO settings for AutomatedLevelSequenceCapture
    # is stored in /Engine/Saved/Config/<Platform>/EditorSettings.ini under the sections labeled "[/Script/MovieSceneCapture.AutomatedLevelSequenceCapture]",
    # and "[/Script/LevelSequence.LevelSequenceBurnInOptions]" .
    # If you happen to upgrade your engine and this file persists, then the old settings will be applied by default to the CDO, and thus to the instance created
    # in Python. If you want to ensure that your Python instances come with default settings set via C++ then you should remove that section from the config file
    # on each users machine, or you should override every possible setting via Python (see below).

    # Create an instance of UAutomatedLevelSequenceCapture
    capture_settings = unreal.AutomatedLevelSequenceCapture()
    capture_settings.level_sequence_asset = unreal.SoftObjectPath(sequencer_asset_path)

    # Invoke Sequencer's Render to Movie. This will throw an exception if a movie render is already
    # in progress, an invalid setting is passed, etc.
    try:
        print("Rendering to movie...")
        unreal.SequencerTools.render_movie(capture_settings, unreal.OnRenderMovieStopped())
    except Exception as e:
        print("Python Caught Exception:")
        print(e)



#####