import pysolr 
import json

core_name = 'ChefRamsey'
solr = pysolr.Solr('http://localhost:8983/solr/'+core_name+'/', timeout=60)

#jsondata = json.load(open('full_format_recipes.json'))
recipes = []
with open('full_format_recipes.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        #fix recipe name and skip if no title
        try:
            rname = p['title']
            rname = rname.replace('/',' ')
            rname = rname.replace('"',' ')
            rname = rname.replace('  ', ' ')
            if rname[0] == ' ':
                rname = rname.split(' ', 1)[1]
        except KeyError:
            continue
        if rname[-1] == ' ':
            rname = rname[:-1]
        print(rname)
        #gen title line
        #recipe = rname + ' recipe.'
        recipe = ''

        #remove numbered directions and combine elements for directions
        dirs = ''
        for dirr in p['directions']:
            #prim remove numbering on directions
            if dirr[0].isdigit():
                dirr = dirr.split(' ', 1)[1]
            dirs = dirs + ' ' + dirr
        #remove parens
        dirs = dirs.replace('(','')
        dirs = dirs.replace('(','')
        if 'Combine all ingredients in a cocktail shaker and shake vigorously. Strain into a cocktail glass.' in dirs: continue
        recipe = recipe + dirs + ' '

        #calories, protien, fat, sodium
        if p['calories']: recipe = recipe + rname + ' has ' + str(p['calories']) + ' calories. '
        if p['protein']:  recipe = recipe + rname + ' has ' + str(p['protein']) + ' grams of protein. '
        if p['fat']:      recipe = recipe + rname + ' has ' + str(p['fat']) + ' grams of fat. '
        if p['sodium']:   recipe = recipe + rname + ' has ' + str(p['sodium']) + ' grams of sodium. '

        #ingredients
        ings = 'The ingredients of ' + rname + ' are'
        for ing in p['ingredients']:
            ings = ings + ' ' + ing + ','
        recipe = recipe + ings[:-1] + '.'

        #description if any
        if p['desc']:
            if p['desc'][-1] != '.':
                recipe = recipe + p['desc'] + '. '
            else:
                recipe = recipe + p['desc'] + ' '

        #categories
        cats = ''
        for cat in p['categories']:
            cats = cats + ' ' + cat.replace('/', ' ')
        recipe = recipe + cats + '.'
        recipes.append({'name':rname,'passage':recipe})
        print('fin')
solr.add(recipes)
