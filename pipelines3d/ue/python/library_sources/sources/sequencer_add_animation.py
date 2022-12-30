import unreal


# sequence_path: str : The level sequence asset path
# actor: obj unreal.Actor : The actor you want to add into (or get from) the sequence asset
# return: obj unreal.SequencerBindingProxy : The actor binding
def getOrAddPossessableInSequenceAsset(sequence_path='', actor=None):
    sequence_asset = unreal.LevelSequence.cast(unreal.load_asset(sequence_path))
    possessable = sequence_asset.add_possessable(object_to_possess=actor)
    return possessable


# animation_path: str : The animation asset path
# possessable: obj unreal.SequencerBindingProxy : The actor binding you want to add the animation on
# return: obj unreal.SequencerBindingProxy : The actor binding
def addSkeletalAnimationTrackOnPossessable(animation_path='', possessable=None):
    # Get Animation
    animation_asset = unreal.AnimSequence.cast(unreal.load_asset(animation_path))
    params = unreal.MovieSceneSkeletalAnimationParams()
    params.set_editor_property('Animation', animation_asset)
    # Add track
    animation_track = possessable.add_track(track_type=unreal.MovieSceneSkeletalAnimationTrack)
    # Add section
    animation_section = animation_track.add_section()
    animation_section.set_editor_property('Params', params)
    animation_section.set_range(0, animation_asset.get_editor_property('sequence_length'))


def addSkeletalAnimationTrackOnActor_EXAMPLE():
    sequence_path = '/Game/S8n-Experimental/x-generated-seq/scene_0000.scene_0000'
    body_anim_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'
    editor_world = unreal.EditorLevelLibrary.get_editor_world()
    print(editor_world)
    all_actors = unreal.GameplayStatics.get_all_actors_of_class(editor_world, unreal.SkeletalMeshActor)
    print(all_actors)
    actor_in_world = all_actors[0] # ()
    possessable_in_sequence = getOrAddPossessableInSequenceAsset(sequence_path, actor_in_world)
    addSkeletalAnimationTrackOnPossessable(body_anim_sequence_path, possessable_in_sequence)


addSkeletalAnimationTrackOnActor_EXAMPLE()