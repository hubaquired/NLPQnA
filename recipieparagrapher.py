import json

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
		with open('recipedocs/' + rname + '.txt', 'w') as newdoc:
			#gen title line
			newdoc.write(rname + ' recipe.')

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
			newdoc.write(dirs + ' ')

			#calories, protien, fat, sodium
			if p['calories']:
				newdoc.write(rname + ' has ' + str(p['calories']) + ' calories. ')
			if p['protein']:
				newdoc.write(rname + ' has ' + str(p['protein']) + ' grams of protein. ')
			if p['fat']:
				newdoc.write(rname + ' has ' + str(p['fat']) + ' grams of fat. ')
			if p['sodium']:
				newdoc.write(rname + ' has ' + str(p['sodium']) + ' grams of sodium. ')

			#ingredients
			ings = 'The ingredients of ' + rname + ' are'
			for ing in p['ingredients']:
				ings = ings + ' ' + ing + ','
			newdoc.write(ings[:-1] + '.')

			#description if any
			if p['desc']:
				if p['desc'][-1] != '.':
					newdoc.write(p['desc'] + '. ')
				else:
					newdoc.write(p['desc'] + ' ')

			#categories
			cats = ''
			for cat in p['categories']:
				cats = cats + ' ' + cat.replace('/', ' ')
			newdoc.write(cats + '.')



		print('fin')
