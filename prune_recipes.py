import json

recipes = []
stop_titles = ['Do-Ahead']
#bigleaftime
with open('full_format_recipes.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        if sum([a in p['title'] for a in stop_titles]):
            print(p['title'])
        else:
            recipes.append(p)
with open('mod_recipes.json','w') as json_file:
    json.dump(recipes,json_file)
