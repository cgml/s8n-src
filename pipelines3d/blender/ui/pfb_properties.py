import bpy

def main(context):
    for obj in context.scene.objects:
        print(obj)

class UIdemo(bpy.types.Operator):
    bl_idname = "object.simpleui"
    bl_label = "Simple Popup Uset Interface"
    bl_options = {'REGISTER', 'UNDO'}
    
    name = bpy.props.StringProperty(name="Name", default="abc")
    
    @classmethod
    def poll(cls, context):
        print('poll', context)
        return context.active_object is not None
    
    def invoke(self, context, event):
        print('invoke', context, event)
        return context.window_manager.invoke_props_popup(self, event)
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(UIdemo)

def unregister():
    bpy.utils.unregister_class(UIdemo)
    
if __name__ == "__main__":
    register()
    
    bpy.ops.object.simpleui('INVOKE_DEFAULT')

