import pysolr 
import json

core_name = ''
solr = pysolr.Solr('http://localhost:8983/solr/+'core_name'+/', timeout=60)

jsondata = json.load(open('full_format_recipes.json'))
values = []
for value in jsondata:
    values.append(value)
solr.add(values)
