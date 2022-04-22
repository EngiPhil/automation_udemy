import requests
import json

"""
odics = '{"K1": "val1", "K2": "val2"}'
json_result = json.loads(odics)
print(json_result)
"""

api_url = 'https://reqres.in/api/users?page=2'
response = requests.get(api_url)
print(response.text)
