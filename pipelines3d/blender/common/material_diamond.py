import bpy

class MaterialDiamond(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = 'shader.diamond_operator' 
    
    def execute(self, context):
        # TODO Reuse existing shader if possible
        material_diamond = bpy.data.materials.new(name="Diamond")
        material_diamond.use_nodes = True
        nodes = material_diamond.node_tree.nodes
        nodes.remove(nodes.get("Principled BSDF"))
        material_output = nodes.get("Material Output")
        material_output.location = (-400, 0)
        
        glass1_node = material_diamond.node_tree.nodes.new(type="ShaderNodeBsdfGlass")
        glass1_node.location = (-600, 0)
        glass1_node.inputs[0].default_value = (1, 0, 0, 1) #RGBA
        glass1_node.inputs[2].default_value = 1.450
        
        glass2_node = material_diamond.node_tree.nodes.new(type="ShaderNodeBsdfGlass")
        glass2_node.location = (-600, -150)
        glass2_node.inputs[0].default_value = (0, 1, 0, 1) #RGBA
        glass2_node.inputs[2].default_value = 1.450
        
        
        glass3_node = material_diamond.node_tree.nodes.new(type="ShaderNodeBsdfGlass")
        glass3_node.location = (-600, -300)
        glass3_node.inputs[0].default_value = (0, 0, 1, 1) #RGBA
        glass3_node.inputs[2].default_value = 1.450
        
        add1_node = material_diamond.node_tree.nodes.new("ShaderNodeAddShader")
        add1_node.location = (-400, -50)
        add1_node.label = "Add 1"
        add1_node.hide = True
        add1_node.select = False
        
        add2_node = material_diamond.node_tree.nodes.new("ShaderNodeAddShader")
        add2_node.location = (-100, -50)
        add2_node.label = "Add 2"
        add2_node.hide = True
        add2_node.select = False
        
        glass4_node = material_diamond.node_tree.nodes.new(type="ShaderNodeBsdfGlass")
        glass4_node.location = (-150, -150)
        glass4_node.inputs[0].default_value = (1, 1, 1, 1) #RGBA
        glass4_node.inputs[2].default_value = 1.450      
        glass4_node.select = False
        
        mix1_node = material_diamond.node_tree.nodes.new("ShaderNodeMixShader")
        mix1_node.location = (200, 0)
        mix1_node.select = False
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
                
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])

        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}
