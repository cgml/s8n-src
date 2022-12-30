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


url = "https://foodanddrink.scotsman.com/wp-content/uploads/2016/08/item-4-6-1024x683.jpg"
print(
f"""curl -i -X POST -H "Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS" -H "X-PF-Store-Id: 6185024"  -T {file_path} https://api.printful.com/files""" #-H "Content-Type:application/json"
)
print(
"""curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS" -H "X-PF-Store-Id: 6185024"  -d "{\\\"url\\\": \\\"https://foodanddrink.scotsman.com/wp-content/uploads/2016/08/item-4-6-1024x683.jpg\\\"}" https://api.printful.com/files""" #-H "Content-Type:application/json"
)
print(
"""curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS" -H "X-PF-Store-Id: 6185024"  -d {"url": "https://foodanddrink.scotsman.com/wp-content/uploads/2016/08/item-4-6-1024x683.jpg"} https://api.printful.com/files""" #-H "Content-Type:application/json"
)

print(
"""curl -i -X POST -H "Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS" -H "X-PF-Store-Id: 6185024"  -d "{\\\"url\": \\\"https://foodanddrink.scotsman.com/wp-content/uploads/2016/08/item-4-6-1024x683.jpg\\\"}" https://api.printful.com/files""" #-H "Content-Type:application/json"
)

print(
"""curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS" -H "X-PF-Store-Id: 6185024"  -d @c:\\tmp\\test.png https://api.printful.com/files""" #-H "Content-Type:application/json"
)


"""

curl --location --request POST 'https://api.printful.com/files' \
--header 'Authorization: Basic {encoded_api_key}' \
--data-raw '{
    "url": "http://www.example.com/files/tshirts/example.psd"
}'"""
# print("""curl --location --request POST 'https://api.printful.com/files' --header 'Authorization: Bearer M4Cbq9IuZINIbWKDl96sHaZbx4N0BkFHgnzgJBYS' --header 'X-PF-Store-Id: 6185024' --data-raw '{"url":""" + f'"{file_path}"' + "}'")

