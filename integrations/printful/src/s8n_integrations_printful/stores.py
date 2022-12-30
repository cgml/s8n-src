import requests
import os
import json

from s8n_integrations_printful.config import *

store_id = "6185024"
headers = config_manager.generated_headers()
result = requests.get(f"https://api.printful.com/stores", headers=headers) #/{store_id}

data = json.loads(result.content)

print('Available stores:')
print(data['result'])


print("""curl -i -X GET -H "Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS" https://api.printful.com/stores""")



