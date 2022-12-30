import requests
import json
import os


KW_ACCESS_TOKEN = "access_token"
KW_DATA_ROOT = "data_root"

config = json.loads(open(os.path.join(os.path.dirname(__file__), "config", "config.json")).read())

printful_token = config[KW_ACCESS_TOKEN]

class ConfigManager:
    def generated_headers(self, store_id = None):
        if not store_id:
            auth_headers = {'Authorization': f"Bearer {printful_token}"}
        else:
            auth_headers = {
                'Authorization': f"Bearer {printful_token}",
                'X-PF-Store-Id': f"{store_id}"
            }
        return auth_headers

    def get_config(self):
        return config

config_manager = ConfigManager()
