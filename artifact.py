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

  
print("PWD :: ")
os.system("pwd > response 2>&1")
print(get_response())


dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}

json = json.dumps(dict)
f = open("dict.json","w")
f.write(json)
f.close()

os.system("cat dict.json > response 2>&1")
print(get_response())

