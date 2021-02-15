import os

import json
print("PWD :: ")
print(os.system("pwd"))

dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}

json = json.dumps(dict)
f = open("dict.json","w")
f.write(json)
f.close()

print(os.system("cat dict.json"))

