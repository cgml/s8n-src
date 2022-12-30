def backup():
    for curve in bpy.data.curves:
        print(curve.name)

    print(bpy.data.curves)

    print(bpy.data.curves['SourceCurve'])

    bpy.data.curves['SourceCurve']

    def duplicate(obj, data=True, actions=True, collection=None):
        obj_copy = obj.copy()
        if data:
            obj_copy.data = obj_copy.data.copy()
        if actions and obj_copy.animation_data:
            obj_copy.animation_data.action = obj_copy.animation_data.action.copy()
        collection.objects.link(obj_copy)
        return obj_copy

    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    cylinder = bpy.context.active_object
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))
    cube = bpy.context.active_object
    bpy.context.active_object.location.z += 1  # same as cube.location.z += 1

    print(cylinder)
    print(cube)

    # new_obj = bpy.data.objects.new(name, mesh)
    # bpy.context.scene.objects.link(new_obj)
    # bpy.ops.object.make_single_user(object = True, obdata = True, material = True,texture = True )

    new_obj = bpy.data.curves.new('SourceCurveR', curve)
    bpy.context.scene.objects.link(new_obj)
    bpy.ops.object.make_single_user(object=True, obdata=True, material=True, texture=True)

    curve = bpy.data.objects['SourceCurveL']
    new_obj = bpy.data.curves.new('SourceCurveR', 'CURVE')

    # bpy.context.scene.objects.link(new_obj)

    # curve.select_set(True)
    # bpy.context.view_layer.objects.active = curve


def test():
    source_curve_l_object = bpy.data.objects['SourceCurveL']

    source_curve_l_object.select_set(True)
    bpy.context.view_layer.objects.active = source_curve_l_object
    source_curve_l_mesh = bpy.ops.object.convert(target='MESH')


def test2():
    # source_curve_l_object = bpy.data.objects['SourceCurveL']

    new_obj = bpy.data.curves.new('SourceCurveR', 'CURVE')
    scene = bpy.context.scene
    scene.collection.objects.link(new_obj)
    # bpy.context.scene.objects.link(new_obj)
    # for c in bpy.data.curves:
    #    print(c)

    # template_ob = bpy.data.objects.get("template")
    # if template_ob:
    #    ob = template_ob.copy()
    #    # link to collection if need be
    #    collection.objects.link(ob)


def main():
    bpy.data.objects['SourceCurveL']

    source_curve_l_obj = bpy.data.objects['SourceCurveL']
    # bpy.data.objects['SourceCurveL'].copy()

    obj = bpy.data.objects['SourceCurveR']

    obj = source_curve_l_obj.copy()
    bpy.context.scene.collection.objects.link(obj)
    obj.select_set(True)
    obj.name = 'SourceCurveR'
    # bpy.context.scene.current_object.name = 'a'

    # obj.location = [1,1,1]
    obj.rotation_euler = [0, 3.14 * 2, 0]

    obj
