import unreal

BASE_PATH = '/Game/S8n-Experimental/MainExample/'

def create_asset(asset_path='', asset_class=None, asset_factory=None):
    asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(base_package_name=asset_path, suffix='')

    if not unreal.EditorAssetLibrary.does_asset_exist(asset_path=asset_path):
        path = asset_path.rsplit('/', 1)[0]
        name = asset_path.rsplit('/', 1)[1]
        return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class=asset_class, factory=asset_factory)
    return unreal.load_asset(asset_path)

def main_example():
    base_path = BASE_PATH
    sequence_path = base_path + 'sequence'
    # generic_assets = [
    #     [, unreal.LevelSequence,   unreal.LevelSequenceFactoryNew()],
    #     [base_path + 'material', unreal.Material,        unreal.MaterialFactoryNew()],
    #     [base_path + 'world',   unreal.World,           unreal.WorldFactory()],
    # ]
    #
    # for asset in generic_assets:
    #     print(create_asset(*asset))

    create_sequence_from_selection(sequence_path)

def create_sequence_from_selection(asset_path, length_seconds=5): # asset_name, length_seconds=5, package_path='/Game/'):
    # sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path, unreal.LevelSequence, unreal.LevelSequenceFactoryNew())

    sequence = unreal.load_asset(asset_path)

    for actor in unreal.SelectedActorIterator(unreal.EditorLevelLibrary.get_editor_world()):
        binding = sequence.add_possessable(actor)

        # Add a transform track for the actor
        transform_track = binding.add_track(unreal.MovieScene3DTransformTrack)
        transform_section = transform_track.add_section()
        transform_section.set_start_frame_seconds(0)
        transform_section.set_end_frame_seconds(length_seconds)

        # Add a visibility track for the actor
        visibility_track = binding.add_track(unreal.MovieSceneVisibilityTrack)
        visibility_track.set_property_name_and_path('bHidden', 'bHidden')
        visibility_section = visibility_track.add_section()
        visibility_section.set_start_frame_seconds(0)
        visibility_section.set_end_frame_seconds(length_seconds)

        # Add a bool simulate physics property track to the root component
        root_component_binding = sequence.add_possessable(actor.root_component)
        root_component_binding.set_parent(binding)

        simulate_physics_track = root_component_binding.add_track(unreal.MovieSceneBoolTrack)
        simulate_physics_track.set_property_name_and_path('bSimulatePhysics', 'BodyInstance.bSimulatePhysics')
        simulate_physics_section = simulate_physics_track.add_section()
        simulate_physics_section.set_start_frame_seconds(0)
        simulate_physics_section.set_end_frame_seconds(length_seconds)

        # Add a dummy vector track for 2 channels
        vector_track = root_component_binding.add_track(unreal.MovieSceneVectorTrack)
        vector_track.set_property_name_and_path('Dummy2Vector', 'Dummy2Vector')
        vector_track.set_num_channels_used(2)
        vector_section = vector_track.add_section()
        vector_section.set_start_frame_seconds(0)
        vector_section.set_end_frame_seconds(length_seconds)

        try:
            camera = unreal.CameraActor.cast(actor)
            camera_cut_track = sequence.add_master_track(unreal.MovieSceneCameraCutTrack)

            # Add a camera cut track for this camera
            camera_cut_section = camera_cut_track.add_section()
            camera_cut_section.set_start_frame_seconds(0)
            camera_cut_section.set_end_frame_seconds(length_seconds)

            camera_binding_id = unreal.MovieSceneObjectBindingID()
            camera_binding_id.set_editor_property("Guid", binding.get_id())
            camera_cut_section.set_editor_property("CameraBindingID", camera_binding_id)

            # Add a current focal length track to the cine camera component
            camera_component = actor.get_cine_camera_component()
            camera_component_binding = sequence.add_possessable(camera_component)
            camera_component_binding.set_parent(binding)
            focal_length_track = camera_component_binding.add_track(unreal.MovieSceneFloatTrack)
            focal_length_track.set_property_name_and_path('CurrentFocalLength', 'CurrentFocalLength')
            focal_length_section = focal_length_track.add_section()
            focal_length_section.set_start_frame_bounded(0)
            focal_length_section.set_end_frame_bounded(0)

        except TypeError:
            pass

        print("{0} is bound as {1}".format(actor, binding.get_id()))

    return sequence


def create_master_level_sequence(asset_name, package_path='/Game/', num_subsequences=1, length_seconds=5):
    master_sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path,
                                                                              unreal.LevelSequence,
                                                                              unreal.LevelSequenceFactoryNew())
    cinematic_shot_track = master_sequence.add_master_track(unreal.MovieSceneCinematicShotTrack)

    shot_start = 0
    shot_len = length_seconds / num_subsequences

    for i in range(num_subsequences):
        subsequence_asset_name = 'shot_' + str(i)
        subsequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(subsequence_asset_name, package_path,
                                                                              unreal.LevelSequence,
                                                                              unreal.LevelSequenceFactoryNew())

        # add a subsection for this subsequence
        subsequence_section = cinematic_shot_track.add_section()
        subsequence_section.set_sequence(subsequence)
        subsequence_section.set_end_frame_seconds(shot_start + shot_len)
        subsequence_section.set_start_frame_seconds(shot_start)
        subsequence_section.set_shot_display_name(subsequence_asset_name)

        # add a camera cut track
        camera_cut_track = subsequence.add_master_track(unreal.MovieSceneCameraCutTrack)
        camera_cut_section = camera_cut_track.add_section()
        camera_cut_section.set_start_frame_seconds(0)
        camera_cut_section.set_end_frame_seconds(length_seconds)

        shot_start = shot_start + shot_len

        # add a binding for the camera
        camera_binding = subsequence.add_spawnable_from_class(unreal.CineCameraActor)
        transform_track = camera_binding.add_track(unreal.MovieScene3DTransformTrack)
        transform_section = transform_track.add_section()
        transform_section.set_start_frame_bounded(0)
        transform_section.set_end_frame_bounded(0)

        # add the binding for the camera cut section
        camera_binding_id = subsequence.make_binding_id(camera_binding, unreal.MovieSceneObjectBindingSpace.LOCAL)
        camera_cut_section.set_camera_binding_id(camera_binding_id)

    return master_sequence


main_example()

