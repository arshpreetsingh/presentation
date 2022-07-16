import json
with open('bse_data_quotes.json','r') as f:
    data = json.loads(f.read())

print(len(data))