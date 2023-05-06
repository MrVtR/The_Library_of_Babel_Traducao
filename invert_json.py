from collections import OrderedDict
import json
  
f = open('./language_en.json',encoding='utf-8')

data = json.load(f)

for idx, item in enumerate(data["ListOfPairs"]):
    data["ListOfPairs"][idx] = OrderedDict(sorted(item.items(), key=lambda x: x[0])) #Ida
    # data["ListOfPairs"][idx] = OrderedDict(sorted(item.items(), key=lambda x: x[0],reverse=True)) #Volta
    print(data["ListOfPairs"][idx])
    print()

output_json = json.dumps(data)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
