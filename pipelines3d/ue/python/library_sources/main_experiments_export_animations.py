import os

import unreal
import library_functions as lf

import importlib
importlib.reload(lf)


#########################################
# OPEN LEVEL
lf.level_load_level_experimental()

editor_world = lf.level_get_editor_world()
print(editor_world)


#########################################
# EXPORT / LOAD ANIMATION DATA
model_character = lf.level_get_actor_by_label('PlayerA')
animation_names = ['Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted']
for animation_name in animation_names:
    print(f'Exporting {animation_name}')
    anim_sequence_path = f'/Game/s8n/animations/mixamo-y-retargeted/{animation_name}'
    os.makedirs('C:/s8n/system/src/x-exported/ue/_exported_animation', exist_ok=True)
    result = lf.level_export_animation_file(
        f'C:/s8n/system/src/x-exported/ue/_exported_animation/{animation_name}.json', model_character, anim_sequence_path
    )
