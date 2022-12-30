import unreal

#your lines to spawn the actor, i did use them as is, nothing changed
actor_class = unreal.CameraRig_Rail

# print(actor_class.rail_spline_component)
actor_location = unreal.Vector(0.0,0.0,0.0)
actor_rotation = unreal.Rotator(0.0,0.0,0.0)
_spawnedActor  = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, actor_rotation)

points = []
for idx in range(1, 20):
    position = [idx * 100.0, 0.0, 0.0]
    print(idx, position)
    arrive = [1.0, 0.0, 0.0]
    leave = [1.0, 0.0, 0.0]
    rotation = [idx*10, idx*10, 0]
    rail_point = unreal.SplinePoint(input_key=idx, position=position, arrive_tangent=arrive,
                                    leave_tangent=leave, rotation=rotation, scale=[1.0, 1.0, 1.0],
                                    type=unreal.SplinePointType.CURVE)
    _spawnedActor.get_rail_spline_component().add_point(rail_point, update_spline=False)
