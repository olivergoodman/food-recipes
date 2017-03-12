# transformations:
# 	- to/from vegetarian
# 	- to/from healthy
# 	- cooking method (ex. from bake to stir-fry)
import re
import random
import copy
import json
from veggies import veg2meat, meat2veg
from transforms import healthy_fats, unhealthy_fats, unhealthy_protein, healthy_protein, unhealthy_dairy, healthy_dairy, unhealthy_salts, healthy_salts, unhealthy_grains, healthy_grains, unhealthy_sugars, healthy_sugars, unhealthy_methods, healthy_methods
from transforms import to_healthy_fats, to_healthy_protein, to_healthy_dairy, to_healthy_salts, to_healthy_sugars, to_healthy_grains, to_healthy_methods 

#	return format for test: 

parsed_vals = {
	"tools": ["", ""],
	"methods": ["grill", "cut"],
	"ingredients": [
	    {
			"preparation": "",
			"descriptor": "",
			"measurement": "pinch",
			"name": "salt",
			"quantity": "1"
	    },
	    {
			"preparation": "",
			"descriptor": "",
			"measurement": "19 ounce",
			"name": "can garbanzo beans, half the liquid reserved",
			"quantity": "1"
	    },
	    {
			"preparation": "",
			"descriptor": "",
			"measurement": "lb",
			"name": "roast tofu",
			"quantity": "1"
	    }],
	"steps": [ 
		{
			"method": "grill",
			"ingredients": ['garlic', 'tofu'],
			"tools": ["knife","spoon"], 
			"text": "grill tofu and then put some garlic on top"
		},
		{
			"method": "",
			"ingredients": ['salt', 'potatos'],
			"tools": [], 
			"text": "test text"
		}]
}


# ------------------------------------------------------------------------------------------------------------------------
# veggie sub:
def transform_to_vegetarian(recipe):
	"""
	given a recipe (in JSON format above),
	returns recipe JSON with both list of ingredients and ingredients in steps changed
	"""

	new_recipe = copy.deepcopy(recipe)

	# update list of ingredients
	for i, ingredient in enumerate(new_recipe['ingredients']):
		name = ingredient['name'].lower()
		#iterate thru keys in the dictionary. if key a substring in ingredient name, replace ingredient name w value
		for key in meat2veg:
			if key in name:
				new_recipe['ingredients'][i]['name'] = name.replace(key, meat2veg[key])

	# update list of ingredients in steps
	for i, step in enumerate(new_recipe['steps']):
		ingredients = step['ingredients']
		for j, ingredient_name in enumerate(ingredients):
			ingredient_name = ingredient_name.lower()
			#iterate thru keys in the dictionary. if key a substring in ingredient name, replace ingredient name w value
			for key in meat2veg:
				if key in ingredient_name:
					new_recipe['steps'][i]['ingredients'][j] = ingredient_name.replace(key, meat2veg[key])

	return new_recipe


def transform_from_vegetarian(recipe):
	"""
	given a vegetarian recipe (in JSON format above),
	returns recipe JSON with both list of ingredients and ingredients in steps changed
	"""

	new_recipe = copy.deepcopy(recipe)

	# update list of ingredients
	for i, ingredient in enumerate(new_recipe['ingredients']):
		name = ingredient['name'].lower()
		#iterate thru keys in the dictionary. if key a substring in ingredient name, replace ingredient name w value
		for key in veg2meat:
			if key in name:
				new_recipe['ingredients'][i]['name'] = name.replace(key, veg2meat[key])

	# update list of ingredients in steps
	for i, step in enumerate(new_recipe['steps']):
		ingredients = step['ingredients']
		for j, ingredient_name in enumerate(ingredients):
			ingredient_name = ingredient_name.lower()
			#iterate thru keys in the dictionary. if key a substring in ingredient name, replace ingredient name w value
			for key in veg2meat:
				if key in ingredient_name:
					new_recipe['steps'][i]['ingredients'][j] = ingredient_name.replace(key, veg2meat[key])

	return new_recipe

# ------------------------------------------------------------------------------------------------------------------------
# to/from health transformation
def transform_to_healthy(recipe):
	healthy_dicts = [to_healthy_fats, to_healthy_protein, to_healthy_dairy, to_healthy_salts, to_healthy_sugars, to_healthy_grains]

	new_recipe = copy.deepcopy(recipe)

	# replace ingredients
	for d in healthy_dicts:
		# update list of ingredients
		for i, ingredient in enumerate(new_recipe['ingredients']):
			name = ingredient['name'].lower()
			#iterate thru keys in the dictionary. if key a substring in ingredient name, replace ingredient name w value
			for key in d:
				if key in name:
					new_recipe['ingredients'][i]['name'] = name.replace(key, d[key])

		# update list of ingredients in steps
		for i, step in enumerate(new_recipe['steps']):
			ingredients = step['ingredients']
			for j, ingredient_name in enumerate(ingredients):
				ingredient_name = ingredient_name.lower()
				#iterate thru keys in the dictionary. if key a substring in ingredient name, replace ingredient name w value
				for key in d:
					if key in ingredient_name:
						new_recipe['steps'][i]['ingredients'][j] = ingredient_name.replace(key, d[key])

	# replace methods
	d = to_healthy_methods
	for key in to_healthy_methods:
		# update list of methods
		for i, method in enumerate(new_recipe['methods']):
			method = method.lower()
			if key in method:
				new_recipe['methods'][i] = method.replace(key, d[key])

		# update method in list of steps
		for i, step in enumerate(new_recipe['steps']):
			methods = step['method']
			for j, method_name in enumerate(methods):
				method_name = method_name.lower()
				#iterate thru keys in the dictionary. if key a substring in method name, replace method name w value
				for key in d:
					if key in method_name:
						new_recipe['steps'][i]['method'][j] = method_name.replace(key, d[key])

	return new_recipe


# ------------------------------------------------------------------------------------------------------------------------
# change cooking method
def replace_methods(vals):
# takes in vals, oldm, newm
	oldm = raw_input('What cooking method do you want to change?    ').lower()
	newm = raw_input ('What do you want to change it into?    ').lower()
	myrec = copy.deepcopy(vals)
	# replace method in steps
	for step in myrec["steps"]:
		for i, method in enumerate(step['method']):
			method = method.lower()
			if method == oldm:
				step['method'][i] = newm
				step["text"] =  step["text"].replace(oldm, newm)
	# replace method in list of methods
	for i, method in enumerate(myrec["methods"]):
		if method.lower() == oldm.lower():
			myrec['methods'][i] = newm

	return myrec

# ------------------------------------------------------------------------------------------------------------------------

#test
print '\n******************** Meat 2 Vegetarian transformation ************************\n'
print json.dumps(transform_to_vegetarian(parsed_vals), sort_keys=True, indent=2)
print '\n******************** Vegetarian 2 Meat transformation ************************\n'
print json.dumps(transform_from_vegetarian(parsed_vals), sort_keys=True, indent=2)
print '\n************************ Healthy transformation ****************************\n'
print json.dumps(transform_to_healthy(parsed_vals), sort_keys=True, indent=2)
print '\n************************ Replace cooking method transformations ****************\n'
print json.dumps(replace_methods(parsed_vals), sort_keys=True, indent=2)