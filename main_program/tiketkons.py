import json

with open("tiket.json", "r") as f:
        data =json.load(f)

print(data)