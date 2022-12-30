import unreal


def populate_track(sequence, track, num_sections=1, section_length_seconds=1):
    result = []
    for i in range(num_sections):
        section = track.add_section()
        section.set_start_frame_seconds(i * section_length_seconds)
        section.set_end_frame_seconds(section_length_seconds)
        result.append(section)
    return result


def create_level_sequence_with_spawnable_camera(asset_name, package_path='/Game/'):
    sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path, unreal.LevelSequence,
                                                                       unreal.LevelSequenceFactoryNew())

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