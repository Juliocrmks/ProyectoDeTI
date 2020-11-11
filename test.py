
import json

with open('jsontest.json','r') as f:
        data = json.load(f)
        for item in data:
            print(data[item][0]['item1']['name'])