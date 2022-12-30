import unreal

# References:
# https://gist.github.com/nafeesb/9482a55e98af3123f512c049533ead1d
# https://www.unrealengine.com/en-US/tech-blog/demystifying-bone-indices
#


# Get the Actor subsystem to grab a selected actor
actor_system = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
actor = actor_system.get_selected_level_actors()[0]

SK = actor.get_components_by_class(unreal.SkeletalMeshComponent)[2]
print(SK.get_socket_location('upperarm_l'))
print(SK)

for idx in range(SK.get_num_bones()):
    print(SK.get_bone_name(idx))
