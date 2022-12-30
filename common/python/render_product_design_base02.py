from typing import Tuple
import os
import bpy
import shutil
import json


LIBRARY_PATH = r"C:\s8n\system\src\pipelines\s8n-alpha\blender\library"
PIPELINES_ROOT = r"C:\s8n\system\src\x-generated\blender\s8n-alpha-pipelines\20220816"

MATERIAL_NAME = "s8n-material-20220814-organic-pattern"
MATERIAL_NAME = "s8n-material-camouflage-simple-01"
MATERIAL_NAME = "s8n-material-camouflage-pattern-02"
MATERIAL_NAME = "s8n-material-camouflage-pattern-04"

PRODUCT_DESIGN_TEMPLATE = "s8n-product-design-template-base-02"
PRODUCT_DESIGN_NAME = 'base-02_20220815-camouflage-04'

pipeline_name = "s8n-pipeline-stage-product-design"

GENERATE_FILES = False


material_path = fr"{LIBRARY_PATH}\materials\{MATERIAL_NAME}\{MATERIAL_NAME}.blend"
product_design_template_path = fr"{LIBRARY_PATH}\products\printful\woman\yoga-pants\product-design-template\{PRODUCT_DESIGN_TEMPLATE}\{PRODUCT_DESIGN_TEMPLATE}.blend"

product_pipeline = fr"{PIPELINES_ROOT}\{pipeline_name}"

product_pipeline_src = fr"{product_pipeline}\src"
os.makedirs(product_pipeline_src, exist_ok=True)

pipeline_material = product_pipeline + r"\material-01.blend"
pipeline_product_design = product_pipeline + r"\product_design.blend"


def get_output_path(product_design_name: str):
    output_path = fr'{PIPELINES_ROOT}\{pipeline_name}\{product_design_name}'
    return output_path


def import_material(name: str):
    with bpy.data.libraries.load(pipeline_material) as (data_from, data_to):
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


def assign_material(material_name: str, obj_texture: str):
    print(f'Assign material {material_name} to {obj_texture}. started.')
    material = bpy.data.materials[material_name]
    bpy.data.objects[obj_texture].active_material = material
    print(f'Assign material {material_name} to {obj_texture}. completed.')


def prepare_blend_files():
    if os.path.exists(pipeline_material):
        os.remove(pipeline_material)
    if os.path.exists(pipeline_product_design):
        os.remove(pipeline_product_design)

    shutil.copy(material_path, pipeline_material)
    shutil.copy(product_design_template_path, pipeline_product_design)


def open_pipeline_file():
    bpy.ops.wm.open_mainfile(filepath=pipeline_product_design)


def render_product_design_part(product_design_name: str, scene_name: str, resolution: Tuple[int, int], resolution_percentage: float):
    bpy.context.window.scene = bpy.data.scenes[scene_name]

    C = bpy.context
    S = C.scene
    R = S.render

    R.use_file_extension = True
    R.filepath = fr'{get_output_path(product_design_name)}\s8n-rendered\{scene_name}_p{resolution_percentage}_'

    R.resolution_x = resolution[0]
    R.resolution_y = resolution[1]
    R.resolution_percentage = resolution_percentage

    R.image_settings.file_format = 'PNG'
    R.fps = 25

    S.frame_start = 1
    S.frame_end = 1

    bpy.ops.render.render(animation=True)


def generate_meta(product_design_name: str):
    product_meta = {
        'name': PRODUCT_DESIGN_NAME,
        'product_design_name': PRODUCT_DESIGN_NAME,
        'materials': [
            MATERIAL_NAME
        ]
    }
    with open(fr'{get_output_path(product_design_name)}\product_meta.json', 'w') as f:
        f.write(json.dumps(product_meta))


def generate_files(percent: int = 100):

    prepare_blend_files()
    open_pipeline_file()

    import_material(name='legs-l0')
    assign_material(material_name='s8n-material-legs-l0', obj_texture='legs-l0')
    render_product_design_part(product_design_name=PRODUCT_DESIGN_NAME, scene_name='legs', resolution=(7040, 7040), resolution_percentage=percent)

    import_material(name='front-weistband-l0')
    assign_material(material_name='s8n-material-front-weistband-l0', obj_texture='front-weistband-l0')
    render_product_design_part(product_design_name=PRODUCT_DESIGN_NAME, scene_name='front-weistband', resolution=(3000, 1050), resolution_percentage=percent)

    import_material(name='back-weistband-l0')
    assign_material(material_name='s8n-material-back-weistband-l0', obj_texture='back-weistband-l0')
    render_product_design_part(product_design_name=PRODUCT_DESIGN_NAME, scene_name='back-weistband', resolution=(2400, 900), resolution_percentage=percent)


generate_files(percent=10)
generate_meta(product_design_name=PRODUCT_DESIGN_NAME)
