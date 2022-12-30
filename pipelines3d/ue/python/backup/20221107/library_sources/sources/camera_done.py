# https://forums.unrealengine.com/t/is-it-possible-to-import-focal-length-animation-onto-a-camera-in-sequencer/131988/11
import unreal

level_sequence = unreal.LevelSequence.cast(unreal.AssetToolsHelpers.get_asset_tools().create_asset(
    asset_name='your_level_sequence_name',
    package_path='/Game/',
    asset_class=unreal.LevelSequence,
    factory=unreal.LevelSequenceFactoryNew()
))

cine_camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CineCameraActor, unreal.Vector())
# Make sure your camera label is the same as in fbx file
cine_camera.set_actor_label('ShotCam')

binding = level_sequence.add_possessable(cine_camera)
level_sequence.add_possessable(cine_camera.get_cine_camera_component())

camera_id = unreal.MovieSceneObjectBindingID()
camera_id.set_editor_property('guid', binding.get_id())
camera_cut_track = level_sequence.add_master_track(unreal.MovieSceneCameraCutTrack)
camera_section = camera_cut_track.add_section()
camera_section.set_range(0.0, 100.0)
camera_section.set_camera_binding_id(camera_id)

import_setting = unreal.MovieSceneUserImportFBXSettings()
import_setting.set_editor_property('create_cameras', False)
import_setting.set_editor_property('force_front_x_axis', False)
import_setting.set_editor_property('match_by_name_only', True)
import_setting.set_editor_property('reduce_keys', False)
import_setting.set_editor_property('reduce_keys_tolerance', 0.001)

world = unreal.EditorLevelLibrary.get_editor_world()
# TODO unreal.SequencerTools.import_fbx(world, level_sequence, [binding], import_setting, 'your/path/to/fbx')


# unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(sequence)
# unreal.LevelSequenceEditorBlueprintLibrary.set_current_time(start_frame)
#
# unreal.SequencerTools.import_fbx(world, sequence, [camera_binding], import_options, fbx_path)
