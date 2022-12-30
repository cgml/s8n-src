import json
import time

from golden_data import GoldenData


class GameplayManager:
    @staticmethod
    def get_current_mcs():
        return int(round(time.time()*1000000))

    def load_gameplay(self):
        return GoldenData.gameplay

gameplay_manager = GameplayManager()
