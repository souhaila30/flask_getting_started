import requests
#r = requests.get("http://127.0.0.1:5000/name")
r = requests.get("http://vcm-3586.vm.duke.edu:5000/name")
print(r.json())
