import json

class MusicManager:
    ALEX_BEROZA_ARTNOW_ANALYSIS = 'C:/s8n/linux-cp/data/output/analysis/audio/v3_s8n/fr60cut_alexberoza_artnow.mp3.json'
    ALEX_BEROZA_ARTNOW_MUSIC = 'C:/s8n/linux-cp/data/output/audio/mp3/fr60cut_alexberoza_artnow.mp3'

    def load_music_analysis(self):
        with open(self.ALEX_BEROZA_ARTNOW_ANALYSIS) as f:
            animation_data = json.loads(f.read())
        return animation_data

    def get_music_path(self):
        return self.ALEX_BEROZA_ARTNOW_MUSIC

music_manager = MusicManager()