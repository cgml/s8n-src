import unreal


def spawn_actor(model_name: str):
    '''
    Adds specified model by `model_name` to the current level
    '''
    actor_class = unreal.EditorAssetLibrary.load_blueprint_class(model_name)
    actor_location = unreal.Vector(0, 0, 0)
    rotation_location = unreal.Rotator(0, 0, 0)
    return unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, rotation_location)


def spawn_elisa_character_to_current_level():
    model_name = "/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ"
    return spawn_actor(model_name)