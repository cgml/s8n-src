import requests
import os

from s8n_integrations_printful.config import *

file_path = os.path.join(config_manager.get_config()[KW_DATA_ROOT],
                         "accounts",
                         "test",
                         "collections",
                         "2022SS-Test",
                         "03-products",
                         "printful",
                         "woman-cloth",
                         "yoga-pants-abstract-blue-01",
                         "template",
                         "test.png"
                         )


# files = {'upload_file':
#              ('s8n-yoga-pants-abstract-blue-01-waist-back.png', open(file_path, 'rb'), 'application/json')}
files = {'upload_file': open(file_path, 'rb')}

data = {
    "type": "default",
    "url": "https://file.io/u7fPrLecwnyc",
    "options": [
        {
            "id": "template_type",
            "value": "native"
        }
    ],
    "filename": "s-file-io-py2.png",
    "visible": True
}
headers = config_manager.generated_headers(store_id="6185024")
#headers['Content-Type'] = 'application/json'
data_str = json.dumps(data)
result = requests.post("https://api.printful.com/files",
                       #files=files,
                       data=data_str,
                       headers=headers)

print(result.content)


