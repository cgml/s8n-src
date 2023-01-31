import logging
import os
import time
import threading
from typing import Dict
import datetime as dt
import unreal
import json
import library_functions as lf

import importlib

import settings

importlib.reload(lf)
importlib.reload(settings)
from settings import app_context



class SequenceInstructionsExecutor:
    # OUTPUT_DIR = "C:/s8n/system/src/x-generated/ue/music-video-20221028/sequences"
    WORK_DIR = '/Game/S8n-Experimental/x-generated-seq/'

    # DATA_DIR = 'C:/s8n/system/src/pipelines/s8n-alpha/ue/python/_data/render_jobs'
    # QUEUE_DIR = f'{DATA_DIR}/queue'

    def process_sequence_instructions(self, sequence_instructions):
        preset = sequence_instructions['preset']
        for scene_data in sequence_instructions['scenes']:
            scene_name = scene_data["scene"]
            level_path = scene_data["level_path"]

            print(f'Processing scene {scene_name}, level {level_path}')
            for sequence_data in scene_data['sequences']:
                sequence_path = sequence_data['sequence_path']
                for render_cut in sequence_data["render_cuts"]:
                    render_cut_id = render_cut['render_cut_id']
                    start_frame = render_cut['start_frame']
                    end_frame = render_cut['end_frame']
                    os.makedirs(app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR, exist_ok=True)
                    rendering_task = {
                        'preset': preset,
                        'level': level_path,
                        'sequence_path': sequence_path,
                        'render_cut_id': render_cut_id,
                        'start_frame': start_frame,
                        'end_frame': end_frame,
                        'output_path': f"{app_context.RENDER_SEQUENCES_DIR}/{scene_name}_{render_cut_id}"

                    }
                    with open(f'{app_context.RENDER_PIPELINE_FRAMES_QUEUE_DIR}/{scene_name}_{render_cut_id}.json', 'w') as f: # {start_frame}_{end_frame}
                        f.write(json.dumps(rendering_task))
