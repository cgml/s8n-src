import unittest
import json
import datetime as dt
import time
import math
from gameplay_manager import gameplay_manager


class GameplayManagerTests(unittest.TestCase):
    def test_current_ts(self):
        print(int(round(time.time()*1000000)))

    def create_gameplay_script(self, level, gameplay):
        result = {}
        for section_idx, entity_name in enumerate(gameplay):
            section_data = {}
            if gameplay[entity_name] == 'SkeletalMesh':
                for item in gameplay['face_animation_sequence']:
                    raise NotImplementedError()
            result[str(section_idx)] = section_data


    def test_create_gameplay(self):
        gameplays = gameplay_manager.load_gameplay()
        self.assertTrue(len(gameplays) == 1)
        self.assertTrue(gameplays[0]['level'] == '/Game/s8n/scenes/experimental-01/experimental-01.experimental-01')



        print(sum([v[1] for v in gameplays[0]["gameplay"]['PlayerA']['body_animation_sequence']]))

        animation_name = 'Rumba_Dancing_Retargeted.Rumba_Dancing_Retargeted'
        animation_data = json.loads(
            open(f'C:/s8n/system/src/x-exported/s8n-alpha/ue/_exported_animation/{animation_name}.json').read())

        