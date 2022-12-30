import bpy
bpy.ops.text.resolve_conflict(resolution='RELOAD')
"""
https://blender.stackexchange.com/questions/92582/scripting-import-assign-material-from-another-blend-file
data_from are just string lists, in this case, the names of materials in the Blend file designated by the path. data_to is a string list of the names of the materials you want to be loaded. So, whatever names you put in data_to.materials will be loaded from the designated Blend file's material data block into the current material data block. After that, you access those materials in the material data block, i.e., bpy.data.materials. So, your code should read:
"""    

from s8n_blender.common.settings import s8nctx


class S8nLibraryManager:

    def import_material(self, source_name: str, name: str, force: bool = True):
        path = f"{s8nctx.BLENDER_LIBRARY_PATH}\\materials\\{source_name}\\{source_name}.blend"
        # path = f"C:\\s8n\\system\\src\\pipelines\\s8n-alpha\\src\\blender\\experiments\\{name}.blend"

        with bpy.data.libraries.load(path) as (data_from, data_to):
            print(f'Loading data: {data_from} -> {data_to}')
            for material in data_from.materials:
                print(f'Loading material: {type(material)} -> {material}')
                if material == 's8n-material':
                    print(f'Found material: {type(material)} -> {material}')

            data_to.materials = ['s8n-material']

        for mat in bpy.data.materials:
            if mat.name == f's8n-material-{name}':
                print(f'Material [s8n-material-{name}] already exists. stopping... ')
                return

        for mat in bpy.data.materials:
            if mat.name == 's8n-material':
                mat.name = f's8n-material-{name}'
                print(f'Imported material: {mat.name}')

    def import_mesh2d(self, source_name: str, name: str):
        # name = "library-object2d-01"
        # path = f"C:\\s8n\\system\\src\\pipelines\\s8n-alpha\\src\\blender\\experiments\\{name}.blend"
        path = f"{s8nctx.BLENDER_LIBRARY_PATH}\\materials\\{source_name}\\{source_name}.blend"

        for obj in bpy.data.objects:
            if obj.name == f's8n-mesh2d-{name}':
                print('already exists. exiting... ')
                return

        with bpy.data.libraries.load(path) as (data_from, data_to):
            print(data_from, data_to)
            for obj in data_from.objects:
                print(type(obj), obj)
                if obj == 's8n-mesh2d':
                    data_to.objects = ['s8n-mesh2d']

        for obj in bpy.data.objects:
            if obj.name == 's8n-mesh2d':
                obj.name = f's8n-mesh2d-{name}'
                print('Imported: ', obj.name)
        for mesh in bpy.data.meshes:
            if mesh.name == 's8n-mesh2d':
                mesh.name = f's8n-mesh2d-{name}'
                print('Imported: ', mesh.name)
            

    def import_object_TBD(self, source_name: str, imported_name: str):
        import bpy
        file_loc = 'C:\\Users\\MyComp\\Documents\\3Dobjects\\obj\\humans\\human_figure_JOINED.obj'
        imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
        obj_object = bpy.context.selected_objects[0] ####<--Fix
        print('Imported name: ', obj_object.name)        

# for obj in bpy.context.scene.objects:


if False:            
    S8nLibraryManager().import_mesh2d()
    bpy.ops.object.add_named(name='s8n-mesh2d-library-object2d-01')
    bpy.context.active_object.name = 'logo1'
    print(bpy.context.active_object)

# bpy.data.meshes['Mesh.001'].name =  f's8n-mesh2d-{name}'
# bpy.context.active_object.data = bpy.    