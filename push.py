import os
import json

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

  

os.system("cat /home/runner/work/codeql_test2/codeql_test2/dict.json > response 2>&1")
print(get_response())
print("##################")
os.system("cat /home/runner/work/codeql_test2/dict.json > response 2>&1")
print(get_response())
