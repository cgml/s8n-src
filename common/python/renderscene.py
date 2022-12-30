import argparse
import bpy
import shutil

# rf'C:\s8n\system\src\x-generated\src\blender\s8n-alpha-pipelines\{}\{}'
# blender_file = r'C:\s8n\system\src\pipelines\s8n-alpha\blender\pipeline\test.blend'
blender_file = r'C:\s8n\system\src\pipelines\s8n-alpha\blender\library\pipelines\pipeline-stage-01-texture\pipeline-stage-01-texture.blend'
bpy.ops.wm.open_pipeline_file(filepath=blender_file)

C = bpy.context
S = C.scene
R = S.render


R.use_file_extension = True
R.filepath = 'C:\\s8n\\system\\src\\rendered\\blender\\s8n-alpha-products\\20220814\\name'

R.resolution_x = 1024
R.resolution_y = 1024

R.image_settings.file_format = 'PNG'
R.fps = 25

S.frame_start = 1
S.frame_end = 1

bpy.ops.render.render(animation=True)


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Render scene')
#     parser.add_argument()