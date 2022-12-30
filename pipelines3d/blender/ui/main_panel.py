import bpy
import sys

bl_info = {
    "name": "Product Designer",
    "author": "Simulation Inc.",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf",
    "description": "Setup scene, adds product and shader",
    "warning": "",
    "doc_url": "",
    "category": "Add Scene",
}

while "c:\\s8n" in sys.path[-1]:
    del sys.path[-1]
s8n_py_path = "c:\\s8n\\system\\src\\pipelines\\s8n-alpha\\src\\python"
sys.path.append(s8n_py_path)
# print(sys.path)

from s8n.managers import *
from s8n.material_diamond import *


# -----------------------------------
# -- OPERATORS
class ProjectManagerOperator(bpy.types.Operator):
    """Project Manager Operator"""     # Use this as a tooltip for menu items and buttons.
    bl_idname = "s8n_project.reset"    # Unique identifier for buttons and menu items to reference.
    bl_label = "Reset Project"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    
    def execute(self, context):
        ProjectManager().setup_project()
        mm = MaterialManager()
        mm.setup_material_scene()
        return {'FINISHED'}  

class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.move_x"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move X by One"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

class CreateCollection(bpy.types.Operator):
    """Create Collection Pattern"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.create_collection"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Create Collection"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        imported_obj = bpy.ops.import_scene.obj(filepath="c:\\s8n\\data\\assets\\3d\\ornaments\\freepik-17996\\ornament-0001.obj")
        print(imported_obj)

        return {'FINISHED'}


# -------------------------------------
# -- MAIN PANEL

class ProductDesignerMainPanel(bpy.types.Panel):
    bl_label = "S8n" 
    bl_idname = "S8N_PT_MAINPANEL" # "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D' #NODE_EDITOR
    bl_region_type = 'UI'
    bl_category = "S8n" # "Shader Library"

    def draw(self, context):
        layout = self.layout

        row1 = layout.row()
        row2 = layout.row()
        row1.label(text="Project Manager")
        row2.column().operator("s8n_project.reset")
        
        col = self.layout.column()
        box = layout.box()
        row = box.row()
        print(PROPS)
        for (prop_name, v) in PROPS:
            print(prop_name, v)
            row.prop(context.scene, prop_name)
            
        box = layout.box()

        row = box.row()
        row.operator("nmssm.operator", icon="PREVIEW_RANGE")
        row.operator("nmssm.operator", icon="PREVIEW_RANGE")
        row.operator("nmssm.operator", icon="PREVIEW_RANGE")
        row = box.row()
        
        layout = self.layout

        layout.operator("material.copy", icon='COPYDOWN')
        layout.operator("object.material_slot_copy")
        layout.operator("material.paste", icon='PASTEDOWN')
        layout.operator("object.material_slot_remove_unused")

#Create uilist collections
#    bpy.types.Scene.uiListCollec = CollectionProperty(type=RECLASS_PG_color)
#    bpy.types.Scene.uiListIndex = IntProperty() #used to store the index of the selected item in the uilist
#    bpy.types.Scene.colorRampPreview = CollectionProperty(type=RECLASS_PG_color_preview)
#    #Add handlers
#    bpy.app.handlers.depsgraph_update_post.append(scene_update)
#    #
#    bpy.types.Scene.analysisMode = EnumProperty(
#        name = "Mode",
#        description = "Choose the type of analysis this material do",
#        items = [('HEIGHT', 'Height', "Height analysis"),
#        ('SLOPE', 'Slope', "Slope analysis"),
#        ('ASPECT', 'Aspect', "Aspect analysis")],
#        update = updateAnalysisMode
#        ) 

# Assign a collection.

# ----
# - COLLECTIONS & PROPERTIES

class SceneSettingItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Test Property", default="Unknown")
    value: bpy.props.IntProperty(name="Test Property", default=22)





class AnimationProp(bpy.types.PropertyGroup):
    name : bpy.props.StringProperty(name='Name', default='')
    enabled : bpy.props.BoolProperty(
        name='Enabled', default=True, description='Export this animation')
    anchor : bpy.props.PointerProperty(
        name='Anchor', type=bpy.types.Object, description='Anim-specific camera anchor')
        


# https://blenderartists.org/t/making-a-dynamic-dropdown-menu-in-a-panel/1380276/2
from bpy.props import EnumProperty, PointerProperty
from bpy.types import Panel, Operator, PropertyGroup

class TEMPL_OT_operator(Operator):
    """ tooltip goes here """
    bl_idname = "nmssm.operator"
    bl_label = "Label of operator"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def execute(self, context):
        print("TEMPL_OT_operator")
        # TODO print(context.scene.scene_propname.my_enum)        
        
        return {'FINISHED'}

CLASSES = [
    ProductDesignerMainPanel,
#    ProjectManagerOperator,
    SceneSettingItem,
    TEMPL_OT_operator,
]



PROPS = [
    ('prefix', bpy.props.StringProperty(name='Prefix', default='Pref')),
    ('suffix', bpy.props.StringProperty(name='Suffix', default='Suff')),
    ('add_version', bpy.props.BoolProperty(name='Add Version', default=False)),
    ('version', bpy.props.IntProperty(name='Version', default=1)),
    ('animations', bpy.props.CollectionProperty(name='Animations', type=AnimationProp)),
    #('SceneSettingItem', bpy.props.CollectionProperty(name='SceneSettingItem', type=SceneSettingItem)),
    
]


def register():

    
    for klass in CLASSES:
        # Registers a subclass in blender - https://docs.blender.org/api/current/bpy.utils.html
        bpy.utils.register_class(klass)

    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)
                
    bpy.types.Scene.my_settings = bpy.props.CollectionProperty(type=SceneSettingItem)

#    # Assume an armature object selected.
#    print("Adding 2 values!")

#    my_item = bpy.context.scene.my_settings.add()
#    my_item.name = "Spam"
#    my_item.value = 1000

#    my_item = bpy.context.scene.my_settings.add()
#    my_item.name = "Eggs"
#    my_item.value = 30

#    for my_item in bpy.context.scene.my_settings:
#        print(my_item.name, my_item.value)

def unregister():
    bpy.utils.unregister_class(SceneSettingItem)

#    bpy.utils.unregister_class(TemplProperties)  
#    del bpy.types.Scene.scene_propname
#    
    for (prop_name, _) in PROPS:
        delattr(bpy.types.Scene, prop_name)

    for klass in CLASSES:
        bpy.utils.unregister_class(klass)


if __name__ == "__main__":
    register()
    


