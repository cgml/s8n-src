import bpy

class ProjectManager:
    KW_SCENE_MATERIAL = "Material"
    KW_SCENE_MODEL = "Model"
    KW_SCENE_PRODUCT = "Product"
    KW_SCENE_VFX = "VFX"
    KW_SCENE_DESIGN_STYLE = "Design Style"

    KW_SCENE_BRAND = "Brand"
    KW_SCENE_MOOD = "Mood"
    KW_SCENE_COLLECTION = "Collection"
    KW_SCENE_ITEM = "Item"
    KW_SCENE_STUDIO = "Studio"
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProjectManager, cls).__new__(cls)
        return cls.instance
    
    def setup_project(self):
        scene = bpy.ops.scene.new(type='NEW')
        bpy.context.scene.name = ProjectManager.KW_SCENE_PRODUCT_DESIGN


    def cleanup_scenes(self):
        old_scenes = [s for s in bpy.data.scenes if s != bpy.context.window.scene]

        for scene in old_scenes:
            bpy.context.window.scene = scene
            bpy.ops.scene.delete()

    def create_scene(self, scene_name):
        bpy.ops.scene.new(type='NEW')
        product_scene = bpy.context.scene
        product_scene.name = scene_name
        bpy.context.window.scene = product_scene

    def setup_project(self):
        self.create_scene(ProjectManager.KW_SCENE_MATERIAL)
        self.cleanup_objects()
        self.cleanup_meshes()
        self.cleanup_scenes()
        self.create_scene(ProjectManager.KW_SCENE_MODEL)
        self.create_scene(ProjectManager.KW_SCENE_PRODUCT)
        self.create_scene(ProjectManager.KW_SCENE_VFX)
        self.create_scene(ProjectManager.KW_SCENE_DESIGN_STYLE)
        self.create_scene(ProjectManager.KW_SCENE_BRAND)
        self.create_scene(ProjectManager.KW_SCENE_MOOD)
        self.create_scene(ProjectManager.KW_SCENE_COLLECTION)
        self.create_scene(ProjectManager.KW_SCENE_ITEM)
        self.create_scene(ProjectManager.KW_SCENE_STUDIO)

    def select_scene(self, scene_name):
        bpy.context.window.scene = bpy.data.scenes[scene_name]
    
    def cleanup_objects(self):
        for object in bpy.data.objects:
            bpy.data.objects.remove(object, do_unlink=True)

    def cleanup_meshes(self):
        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh, do_unlink=True)


class MaterialManager:
    KW_MATERIAL_PLANE = 'Material Plane'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MaterialManager, cls).__new__(cls)
        return cls.instance

    def setup_material_scene(self):
        ProjectManager().select_scene(ProjectManager.KW_SCENE_MATERIAL)
        bpy.ops.mesh.primitive_plane_add(size=2, 
            enter_editmode=False, 
            align='WORLD', 
            location=(0, 0, 0), 
            scale=(1, 1, 1))
        bpy.context.selected_objects[0].name = MaterialManager.KW_MATERIAL_PLANE        


ProjectManager().setup_project()
mm = MaterialManager()
mm.setup_material_scene()
