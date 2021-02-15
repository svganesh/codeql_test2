import os
import json
import requests


def get_response():
    msg = ""
    with open("response", "r") as file:
        msg = file.read()
        file.close()
    os.remove("response")
    if msg == "":
        with open("error", "r") as file:
            msg = file.read()
            file.close()
        os.remove("error")
    return msg

 

url = 'https://http-intake.logs.datadoghq.com/v1/input'
with open('/home/runner/work/codeql_test2/codeql_test2/dict.json') as f:
    json_obj = json.load(f)
x = requests.post(url, data = json_obj, headers={'DD-API-KEY':os.environ["DD_API_KEY"], 'Content-Type':'application/json'})

print(x.text)
