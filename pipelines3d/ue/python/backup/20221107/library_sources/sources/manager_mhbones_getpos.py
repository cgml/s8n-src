# TODO - DOCUMENT.
# WORKS! - PRINTS OUT SPECIFIC BONE INFORMATION BY TIME
import unreal

# https://forums.unrealengine.com/t/analizying-animation-bones-location-with-python/147061

anim_sequence_path = '/Game/s8n/animations/mixamo-y-retargeted/Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'

myanim = unreal.load_asset(anim_sequence_path) ## Load animation sequence asset
obj_loc = unreal.Vector(-7800,-900,200)
# TODO obj_anim = unreal.EditorLevelLibrary.spawn_actor_from_object(myanim, obj_loc, (0.0,-90,0)) ## Spawn animation into game world (Editor)


# Get the Actor subsystem to grab a selected actor
actor_system = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
actor = actor_system.get_selected_level_actors()[0]
print(actor.get_components_by_class(unreal.SkeletalMeshComponent))

sk_mesh_body = None
# sk_mesh = unreal.load_asset("/Game/MetaHumans/elisa-001-f1-005/BP_elisa-001-f1-005-HQ.BP_elisa-001-f1-005-HQ")
for sk_mesh in actor.get_components_by_class(unreal.SkeletalMeshComponent):
    if 'Body' in str(sk_mesh):
        sk_mesh_body = sk_mesh

if sk_mesh_body is None:
    exit(0)
playRate=0.5
animTime=2
idx = 0
for idx in range(10):
    animTime = idx / 10.0
    # TODO / check if not necessary and clean sk_mesh_body.set_position(position=animTime, fire_notifies=True)
    sk_mesh_body.override_animation_data(anim_to_play=myanim, is_looping=True, is_playing=True, position=animTime, play_rate=playRate)  ## Set position within animation sequence
    for idbone in range(sk_mesh_body.get_num_bones()):
        bone_name = sk_mesh_body.get_bone_name(idbone)
        bone_loc = sk_mesh_body.get_socket_location(bone_name)  ## Get bone location
        print("Animation time: "+str(animTime) + f"- {bone_name}: "+str(bone_loc))

unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence()

# unreal.EditorLevelLibrary.destroy_actor(obj_anim) ## Destroy spawned animation in Editor.

