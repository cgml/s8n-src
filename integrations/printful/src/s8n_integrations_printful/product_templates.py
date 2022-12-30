import requests
import json
import os
from s8n_integrations_printful.config import *

result = requests.get("https://api.printful.com/product-templates", headers=config_manager.generated_headers())

product_templates = json.loads(result.content)

print(result.content)
