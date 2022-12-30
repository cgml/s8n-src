from typing import List, Dict

import unreal
import json
import os

from settings import app_context

current_dir_path = os.path.dirname(__file__)



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

def level_export_animation_file(output_path: str, model_character, anim_sequence_path: str, play_rate: float = 1.0):
    result = level_export_animation(model_character, anim_sequence_path, play_rate)
    with open(output_path, 'w') as f:
        f.write(json.dumps(result))
    return  result

def _from_vector_to_list(v):
    return [v.x, v.y, v.z]

def _from_list_to_vector(l):
    return unreal.Vector(l[0], l[1], l[2])


def level_export_animation(model_character, anim_sequence_path: str, play_rate: float = 1.0) -> dict:
    # anim_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'

    animation_obj = unreal.load_asset(anim_sequence_path)  ## Load animation sequence asset

    frame_rate_nom = animation_obj.get_editor_property('target_frame_rate').numerator
    frame_rate_denom = animation_obj.get_editor_property('target_frame_rate').denominator
    frame_rate = frame_rate_nom / frame_rate_denom
    number_of_sampled_frames = animation_obj.get_editor_property('number_of_sampled_frames')
    sequence_length = animation_obj.get_editor_property('sequence_length')
    print(f'frame_rate_nom={frame_rate_nom}') # frame rate
    print(f'frame_rate_denom={frame_rate_denom}')
    print(f'frame_rate={frame_rate}')
    print(f'number_of_sampled_frames={number_of_sampled_frames}')  # number of frames
    print(f'sequence_length={sequence_length}') # seconds ~= # frames / frame rate
    print(f'animation_obj={animation_obj}')

    sk_mesh_body = None
    for sk_mesh in model_character.get_components_by_class(unreal.SkeletalMeshComponent):
        if 'Body' in str(sk_mesh):
            sk_mesh_body = sk_mesh

    if sk_mesh_body is None:
        exit(0)

    result = {}
    for frame_idx in range(number_of_sampled_frames):
        animation_time = frame_idx * 1.0 / frame_rate
        # TODO / check if not necessary and clean sk_mesh_body.set_position(position=animTime, fire_notifies=True)
        sk_mesh_body.override_animation_data(
            anim_to_play=animation_obj, is_looping=True, is_playing=True, position=animation_time, play_rate=play_rate
        )
        result[frame_idx] = { 'animation_time_sec': animation_time, "bones":{}}
        for idbone in range(sk_mesh_body.get_num_bones()):
            bone_name = sk_mesh_body.get_bone_name(idbone)
            bone_location = sk_mesh_body.get_socket_location(bone_name)
            bone_transform = sk_mesh_body.get_socket_transform(bone_name)
            bone_rotation = sk_mesh_body.get_socket_rotation(bone_name)
            result[frame_idx]["bones"][str(bone_name)] = {
                'bone_location': [bone_location.x, bone_location.y, bone_location.z],
                # 'bone_transform': _from_vector_to_list(bone_transform),
                'bone_rotation': [bone_rotation.pitch, bone_rotation.yaw, bone_rotation.roll]
            }
    sk_mesh_body.override_animation_data(None)
    return result

##################################
##### SEQUENCER
def sequencer_load_sequence(sequence_path):
    sequence = unreal.load_asset(sequence_path, unreal.LevelSequence)
    return sequence


def sequencer_set_working_range(sequence, start_sec, end_sec):
    sequence.set_work_range_start(start_sec)
    sequence.set_view_range_start(start_sec)
    sequence.set_work_range_end(end_sec)
    sequence.set_view_range_end(end_sec)

def sequencer_set_range(sequence, start_sec, end_sec):
    sequence.set_playback_start_seconds(start_sec)
    sequence.set_playback_end_seconds(end_sec)

    # sequence.get_playback_range().set_start_seconds(start_sec)
    # sequence.get_playback_range().set_end_seconds(end_sec)

def sequencer_set_range_frames(sequence, start_frame, end_frame):
    sequence.set_playback_start(start_frame)
    sequence.set_playback_end(end_frame)
    #
    # sequence.get_playback_range().set_start_frame(start_frame)
    # sequence.get_playback_range().set_end_frame(end_frame)


def sequencer_create_camera_cut(
        level_sequence, cine_camera, start_frame: int, end_frame: int, camera_section_data: Dict, focal_length: int = 50, demo = False
):
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
    # TODO add properties to camera_section_data
    camera_component_binding = level_sequence.add_possessable(cine_camera.get_cine_camera_component())
    camera_component_binding.set_parent(camera_binding)

    camera_component_binding.set_display_name('CurrentFocalLength')

    # Add a focal length track
    # TODO Properties
    focal_length_track = camera_component_binding.add_track(unreal.MovieSceneFloatTrack)
    focal_length_track.set_property_name_and_path('CurrentFocalLength', 'CurrentFocalLength')
    focal_length_section = focal_length_track.add_section()
    focal_length_section.set_start_frame_bounded(start_frame)
    focal_length_section.set_end_frame_bounded(end_frame)

    # TODO for frame_idx in range(start_frame, end_frame+1):
    for channel in focal_length_section.find_channels_by_type(unreal.MovieSceneScriptingFloatChannel):
        print(f'For camera cut with start {start_frame} end {end_frame} frames. scripting float channel {channel}')
        channel.add_key(unreal.FrameNumber(start_frame), focal_length)
        channel.add_key(unreal.FrameNumber(end_frame), focal_length)

    ## 3. TRANSFORM TRACK SETUP
    # Add a transform track
    camera_transform_track = camera_binding.add_track(unreal.MovieScene3DTransformTrack)

    # camera_track.add_track(MovieScene3DTransformTrack)
    transform_section = camera_transform_track.add_section()
    transform_section.set_range(start_frame, end_frame)

    transform_channels = transform_section.get_all_channels()
    # print("TRANSFORM CHANNELS = ", transform_channels)

    if camera_section_data:
        for frame_idx in range(start_frame, end_frame+1):
            frame_idx_str = str(frame_idx)
            if frame_idx_str in camera_section_data["transformations"]:
                frame_data = camera_section_data["transformations"][frame_idx_str]
                print(f'Update transformations {frame_data}')
                for idc in range(6):
                    value = camera_section_data["transformations"][frame_idx_str][idc]
                    transform_channels[idc].add_key(unreal.FrameNumber(frame_idx), value)

    if demo:
        for frame_idx in range(start_frame, end_frame+1):
            # x, y, z, roll, pitch, yaw = camera_section_data[str(frame_idx)]['positions']
            for idc in range(6):
                # value = camera_section_data[str(frame_idx)]['positions'][idc]
                transform_channels[0].add_key(unreal.FrameNumber(frame_idx), -100)
                transform_channels[idc].add_key(unreal.FrameNumber(frame_idx), 0)

def camera_transition(level_sequence, camera_actor, start_frame, end_frame):

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
    focal_length_section.set_start_frame_bounded(start_frame)
    focal_length_section.set_end_frame_bounded(end_frame)

    for channel in focal_length_section.find_channels_by_type(unreal.MovieSceneScriptingFloatChannel):
        channel.set_default(60.0)

    # Add a transform track
    camera_transform_track = camera_binding.add_track(unreal.MovieScene3DTransformTrack)

    # camera_track.add_track(MovieScene3DTransformTrack)
    transform_section = camera_transform_track.add_section()
    transform_section.set_range(start_frame, end_frame)

    transform_channels = transform_section.get_all_channels()
    print("TRANSFORM CHANNELS = ", transform_channels)

    for idc in range(6):
        k = transform_channels[idc].add_key(unreal.FrameNumber(0), 0)

    for idx in range(start_frame, end_frame):
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

def sequencer_delete_sequence(sequence_path):
    unreal.EditorAssetLibrary.delete_asset(sequence_path)

def sequencer_save_sequence(sequence_path):
    unreal.EditorAssetLibrary.save_asset(sequence_path)

def sequencer_refresh_current_level_sequence():
    '''
    Refresh to visually see the new binding added
    '''
    unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence()

def sequence_add_player_track(sequence, player):
    actor_track = sequence.add_possessable(player)
    return actor_track

def sequencer_add_animation_to_animation_track(anim_track, animation_path, range_start_frame, range_end_frame, row_index):
    anim_track = anim_track.add_track(unreal.MovieSceneSkeletalAnimationTrack)
    anim_sequence_section = anim_track.add_section()
    anim_sequence_section.set_range(range_start_frame, range_end_frame)
    run_animation = unreal.AnimSequence.cast(unreal.load_asset(animation_path))
    anim_sequence_section.params.animation = run_animation
    anim_sequence_section.set_row_index(row_index)
    return anim_sequence_section


def sequencer_add_animation_track(sequence, model_character, animation_path: str, range_start, range_end, row_index):
    """
    THAT METHOD DOESN"T WORK BECAYSE MODEL_CHARACTER MUST BE BODY OR FACE
        -
        - animation_path - e.g.
            '/Game/s8n/animations/mixamo-y-retargeted/Running03_InPlace_O00_Retargeted1'
            run_animation = unreal.AnimSequence.cast(unreal.load_asset(animation_path))

    """
    actor_track = sequence.add_possessable(model_character)
    anim = actor_track.add_track(unreal.MovieSceneSkeletalAnimationTrack)

    anim_sequence = anim.add_section()
    anim_sequence.set_range(range_start, range_end)
    run_animation = unreal.AnimSequence.cast(unreal.load_asset(animation_path))
    anim_sequence.params.animation = run_animation
    anim_sequence.set_row_index(row_index)


##################################
###### RIG
def sequencer_add_actor(level_sequence, actor):
    actor_binding = level_sequence.add_possessable(actor)
    return actor_binding

def get_actor_body(actor):
    actor_body = None
    for component in actor.get_components_by_class(unreal.SkeletalMeshComponent):
        if component.get_fname() == "Body":
            actor_body = component
    return actor_body


def add_body_binding_track(level_sequence, actor):
    actor_body = get_actor_body(actor=actor)
    body_component_binding = level_sequence.add_possessable(actor_body)
    return body_component_binding

def get_actor_face(actor):
    actor_face = None
    for component in actor.get_components_by_class(unreal.SkeletalMeshComponent):
        if component.get_fname() == "Face":
            actor_face = component
    return actor_face

def add_face_binding_track(level_sequence, actor):
    actor_face = get_actor_face(actor)
    face_component_binding = level_sequence.add_possessable(actor_face)
    return face_component_binding

def add_body_rig(level, level_sequence, actor):
    body_component_binding = add_body_binding_track(level_sequence, actor)
    body_rig = unreal.load_asset("/Game/MetaHumans/Common/Common/MetaHuman_ControlRig")
    body_rig_class = body_rig.get_control_rig_class()
    body_rig_track = unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track(level, level_sequence,
                                                                                        body_rig_class,
                                                                                        body_component_binding)
    body_rig_section = body_rig_track.get_sections()[0]
    body_rig_channels = body_rig_section.get_all_channels()
    return body_rig_section

def add_face_rig(level, level_sequence, actor):
    face_component_binding = add_face_binding_track(level_sequence, actor) # level_sequence.add_possessable(actor_face)
    face_rig = unreal.load_asset('/Game/MetaHumans/Common/Face/Face_ControlBoard_CtrlRig.Face_ControlBoard_CtrlRig')
    face_rig_class = face_rig.get_control_rig_class()
    face_rig_track = unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track(level, level_sequence,
                                                                                        face_rig_class,
                                                                                        face_component_binding)
    face_rig_section = face_rig_track.get_sections()[0]
    face_rig_channels = face_rig_section.get_all_channels()
    return face_rig_section

##################################
##### EDITOR
def editor_open_level_sequence(sequence):
    unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(sequence)

def get_asset_path(asset):
    return unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)


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


def on_render_movie_finished(success):
    print("Movie has finished rendering. Python can now invoke another movie render if needed. Success: " + str(success))
    if app_context.render_callback is not None:
        print("  - Executing rendering callback")
        app_context.render_callback()


on_finished_callback = unreal.OnRenderMovieStopped()
on_finished_callback.bind_callable(on_render_movie_finished)


def render_sequence_to_images(sequencer_asset_path, output_path, resolution_width=3964, resolution_height=2048):

    # 1) Create an instance of our UAutomatedLevelSequenceCapture and override all of the settings on it. This class is currently
    # set as a config class so settings will leak between the Unreal Sequencer Render-to-Movie UI and this object. To work around
    # this, we set every setting via the script so that no changes the user has made via the UI will affect the script version.
    # The users UI settings will be reset as an unfortunate side effect of this.
    capture_settings = unreal.AutomatedLevelSequenceCapture()

    # Set all POD settings on the UMovieSceneCapture
    capture_settings.settings.output_directory = unreal.DirectoryPath(output_path) # "../../../QAGame/Saved/VideoCaptures/"

    # If you game mode is implemented in Blueprint, load_asset(...) is going to return you the C++ type ('Blueprint') and not what the BP says it inherits from.
    # Instead, because game_mode_override is a TSubclassOf<AGameModeBase> we can use unreal.load_class to get the UClass which is implicitly convertable.
    # ie: capture_settings.settings.game_mode_override = unreal.load_class(None, "/Game/AI/TestingSupport/AITestingGameMode.AITestingGameMode_C")

    # NEW >
    capture_settings.settings.cinematic_mode = True
    capture_settings.settings.resolution = unreal.CaptureResolution(3964, 2048)
    ##

    capture_settings.settings.game_mode_override = None
    capture_settings.settings.output_format = "output"  # {world}"
    capture_settings.settings.overwrite_existing = True
    capture_settings.settings.use_relative_frame_numbers = False
    capture_settings.settings.handle_frames = 0
    capture_settings.settings.zero_pad_frame_numbers = 4
    # If you wish to override the output framerate you can use these two lines, otherwise the framerate will be derived from the sequence being rendered
    capture_settings.settings.use_custom_frame_rate = True
    capture_settings.settings.custom_frame_rate = unreal.FrameRate(30, 1)
    capture_settings.settings.resolution.res_x = resolution_width
    capture_settings.settings.resolution.res_y = resolution_height
    capture_settings.settings.enable_texture_streaming = False
    capture_settings.settings.cinematic_engine_scalability = True
    capture_settings.settings.cinematic_mode = True
    capture_settings.settings.allow_movement = False  # Requires cinematic_mode = True
    capture_settings.settings.allow_turning = False  # Requires cinematic_mode = True
    capture_settings.settings.show_player = False  # Requires cinematic_mode = True
    capture_settings.settings.show_hud = False  # Requires cinematic_mode = True
    capture_settings.use_separate_process = False
    capture_settings.close_editor_when_capture_starts = False  # Requires use_separate_process = True
    capture_settings.additional_command_line_arguments = "-NOSCREENMESSAGES"  # Requires use_separate_process = True
    capture_settings.inherited_command_line_arguments = ""  # Requires use_separate_process = True

    # Set all the POD settings on UAutomatedLevelSequenceCapture
    capture_settings.use_custom_start_frame = False  # If False, the system will automatically calculate the start based on sequence content
    capture_settings.use_custom_end_frame = False  # If False, the system will automatically calculate the end based on sequence content
    capture_settings.custom_start_frame = unreal.FrameNumber(0)  # Requires use_custom_start_frame = True
    capture_settings.custom_end_frame = unreal.FrameNumber(0)  # Requires use_custom_end_frame = True
    capture_settings.warm_up_frame_count = 0.0
    capture_settings.delay_before_warm_up = 0
    capture_settings.delay_before_shot_warm_up = 0.0
    capture_settings.write_edit_decision_list = True

    # Tell the capture settings which level sequence to render with these settings. The asset does not need to be loaded,
    # as we're only capturing the path to it and when the PIE instance is created it will load the specified asset.
    # If you only had a reference to the level sequence, you could use "unreal.SoftObjectPath(mysequence.get_path_name())"
    capture_settings.level_sequence_asset = unreal.SoftObjectPath(sequencer_asset_path)

    # To configure the video output we need to tell the capture settings which capture protocol to use. The various supported
    # capture protocols can be found by setting the Unreal Content Browser to "Engine C++ Classes" and filtering for "Protocol"
    # ie: CompositionGraphCaptureProtocol, ImageSequenceProtocol_PNG, etc. Do note that some of the listed protocols are not intended
    # to be used directly.
    # Right click on a Protocol and use "Copy Reference" and then remove the extra formatting around it. ie:
    # Class'/Script/MovieSceneCapture.ImageSequenceProtocol_PNG' gets transformed into "/Script/MovieSceneCapture.ImageSequenceProtocol_PNG"
    # Class'/Script/MovieSceneCapture.ImageSequenceProtocol_JPEG' gets transformed into "/Script/MovieSceneCapture.ImageSequenceProtocol_JPEG"
    protocol_type = unreal.load_class(None, "/Script/MovieSceneCapture.ImageSequenceProtocol_JPG")
    capture_settings.set_image_capture_protocol_type(protocol_type=protocol_type)

    # After we have set the capture protocol to a soft class path we can start editing the settings for the instance of the protocol that is internallyc reated.
    capture_settings.get_image_capture_protocol().compression_quality = 100


    # TODO ANTIALIASING!

    WATERMARK = False
    if WATERMARK:
        # The other complex settings is the burn-in. Create an instance of the LevelSequenceBurnInOptions which is used to
        # specify if we should use a burn in, and then which settings.
        burn_in_options = unreal.LevelSequenceBurnInOptions()
        burn_in_options.use_burn_in = True

        # You have to specify a path to a class to use for the burn in (if use_burn_in = True), and this class specifies a UClass to define the
        # settings object type. We've created a convinence function which takes the class path, loads the class at that path and assigns it to
        # the Settings object.
        burn_in_options.set_burn_in(unreal.SoftClassPath("/Engine/Sequencer/DefaultBurnIn.DefaultBurnIn_C"))

        # The default burn in is implemented entirely in Blueprint which means that the method we've been using to set properties will not
        # work for it. The python bindings that turn bSomeVariableName into "some_variable_name" only work for C++ classes with
        # UPROPERTY(BlueprintReadWrite) marked fields. Python doesn't know about the existence of Blueprint classes and their fields, so we
        # have to use an alternative method.
        burn_in_options.settings.set_editor_property('TopLeftText', "{FocalLength}mm,{Aperture},{FocusDistance}")
        burn_in_options.settings.set_editor_property('TopCenterText', "{MasterName} - {Date} - {EngineVersion}")
        burn_in_options.settings.set_editor_property('TopRightText',
                                                     "{TranslationX} {TranslationY} {TranslationZ}, {RotationX} {RotationY} {RotationZ}")

        burn_in_options.settings.set_editor_property('BottomLeftText', "{ShotName}")
        burn_in_options.settings.set_editor_property('BottomCenterText', "{hh}:{mm}:{ss}:{ff} ({MasterFrame})")
        burn_in_options.settings.set_editor_property('BottomRightText', "{ShotFrame}")

        # Load a Texture2D asset and assign it to the UTexture2D reference that Watermark is.
        # burn_in_settings.set_editor_property('Watermark', None)
        # Note that this example creates a really obvious watermark (a big blurry green smiley face) just so that you know it's working!
        burn_in_options.settings.set_editor_property('Watermark', unreal.load_asset("/Engine/EngineResources/AICON-Green"))
        burn_in_options.settings.set_editor_property('WatermarkTint', unreal.LinearColor(1.0, 0.5, 0.5,
                                                                                         0.5))  # Create a FLinearColor to tint our Watermark

        # Assign our created instances to our original capture_settings object.
        capture_settings.burn_in_options = burn_in_options

    # Finally invoke Sequencer's Render to Movie functionality. This will examine the specified settings object and either construct a new PIE instance to render in,
    # or create and launch a new process (optionally shutting down your editor).

    unreal.SequencerTools.render_movie(capture_settings, on_finished_callback)






### AA RENDERING


def movie_error(pipeline_executor, pipeline_with_error, is_fatal, error_text):
    print(pipeline_executor)
    print(pipeline_with_error)
    print(is_fatal)
    print(error_text)
    app_context.render_callback()

def movie_finished(pipeline_executor, success):
    print(pipeline_executor)
    print(success)
    app_context.render_callback()

error_callback = unreal.OnMoviePipelineExecutorErrored()
error_callback.add_callable(movie_error)

finished_callback = unreal.OnMoviePipelineExecutorFinished()
finished_callback.add_callable(movie_finished)

def render_sequence_to_images_aa(level_path, sequence_path, output_dir, resolution_width=3840, resolution_height=2160, spatial_sample_count=32):
    # umap = '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01'
    # level_sequence = '/Game/S8n-Experimental/x-generated-seq/scene_0000.scene_0000'

    # outdir = "C:/s8n/system/src/x-generated/ue/tmp"  # os.path.abspath(os.path.join(unreal.Paths().project_dir(), 'out'))
    # fps = 60
    # frame_count = 120

    # Get movie queue subsystem for editor.
    subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
    q = subsystem.get_queue()
    executor = unreal.MoviePipelinePIEExecutor()

    # Optional: empty queue first.
    for j in q.get_jobs():
        q.delete_job(j)

    # Create new movie pipeline job
    job = q.allocate_new_job(unreal.load_class(None, "/Script/MovieRenderPipelineCore.MoviePipelineExecutorJob"))
    job.set_editor_property('map', unreal.SoftObjectPath(level_path))
    job.set_editor_property('sequence', unreal.SoftObjectPath(sequence_path))

    c = job.get_configuration()
    render_pass_settings = c.find_or_add_setting_by_class(unreal.MoviePipelineDeferredPassBase)
    output_setting: unreal.MoviePipelineOutputSetting = c.find_or_add_setting_by_class(
        unreal.MoviePipelineOutputSetting)
    output_setting.output_directory = unreal.DirectoryPath(output_dir)
    output_setting.file_name_format = 'output.{frame_number}'
    output_setting.output_resolution.x = resolution_width
    output_setting.output_resolution.y = resolution_height
    # png_setting=c.find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_PNG)
    jpg_setting = c.find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_JPG)
    aa_settings: unreal.MoviePipelineAntiAliasingSetting = c.find_or_add_setting_by_class(
        unreal.MoviePipelineAntiAliasingSetting)
    print(aa_settings)
    aa_settings.spatial_sample_count = spatial_sample_count
    aa_settings.temporal_sample_count = 1
    aa_settings.override_anti_aliasing = True
    aa_settings.anti_aliasing_method = unreal.AntiAliasingMethod.AAM_NONE


    executor = subsystem.render_queue_with_executor(unreal.MoviePipelinePIEExecutor)
    if executor:
        print('Setting errorr callback and finishied delegate')
        executor.set_editor_property('on_executor_errored_delegate', error_callback)
        executor.set_editor_property('on_executor_finished_delegate', finished_callback)

#
# def render_with_config(sequence):
#
#     config = unreal.load_asset('/Game/S8n-Experimental/Presets/MovieRenderAntiAliasingConfig.MovieRenderAntiAliasingConfig')
#     unreal.MoviePipelineExecutorJob.set_configuration(config)
