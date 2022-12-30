import bpy
 
 
 
class ADDONNAME_PT_TemplatePanel(bpy.types.Panel):
    bl_label = "Name of the Panel"
    bl_idname = "ADDONNAME_PT_TemplatePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Template Tab"
    
    preset_enum : bpy.props.EnumProperty(
        name="",
        description="Select an option",
        items = [
            ('OP1',"Cube", "Add a cube to the scene"),
            ('OP2',"Sphere", "Add a sphere to the scene")            
        ]
        
    )
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("wm.template_operator")
        #layout.prop(self, "preset_enum")
        
 
 
 
 
 
class ADDONAME_OT_TemplateOperator(bpy.types.Operator):
    bl_label = "Template Operator"
    bl_idname = "wm.template_operator"
    
    
    preset_enum : bpy.props.EnumProperty(
        name="",
        description="Select an option",
        items = [
            ('OP1',"Cube", "Add a cube to the scene"),
            ('OP2',"Sphere", "Add a sphere to the scene")            
        ]
        
    )
    
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "preset_enum")
    
    def execute(self, context):
        if self.preset_enum == 'OP1':
            print('OP1')
        if self.preset_enum == 'OP2':
            print('OP2')
            
        return {'FINISHED'}    
 
 
 
 
 
 
 
 
classes = [ADDONNAME_PT_TemplatePanel, ADDONAME_OT_TemplateOperator]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
 
if __name__ == "__main__":
    register()