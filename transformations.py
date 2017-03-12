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
  "steps": [
    {
      "text": "Saute onion in 2 tablespoons olive oil in a skillet over medium heat until onion is translucent, about 5 minutes",
      "secondary_methods": [],
      "tools": [
        "skillet",
        "spoon",
        "tablespoon"
      ],
      "primary_methods": [
        "SAUTE"
      ],
      "ingredients": [
        "onion",
        "olive oil"
      ]
    },
    {
      "text": "Stir garlic into onion and turn off heat",
      "secondary_methods": [],
      "tools": [],
      "primary_methods": [
        "STIR"
      ],
      "ingredients": [
        "cloves garlic",
        "onion"
      ]
    },
    {
      "text": "Transfer onion mixture to a large mixing bowl",
      "secondary_methods": [
        "MIX"
      ],
      "tools": [
        "bowl",
        "mixing bowl"
      ],
      "primary_methods": [],
      "ingredients": [
        "onion"
      ]
    },
    {
      "text": "Stir ground beef, ricotta cheese, parsley, egg, kosher salt, black pepper, and cayenne pepper with onion mixture until almost combined; stir in bread crumbs and continue to mix until thoroughly blended",
      "secondary_methods": [
        "BLEND",
        "MIX"
      ],
      "tools": [],
      "primary_methods": [
        "STIR"
      ],
      "ingredients": [
        "tofu",
        "milk ricotta cheese",
        "parsley",
        "egg",
        "kosher salt",
        "black pepper",
        "cayenne pepper",
        "onion",
        "bread crumbs"
      ]
    },
    {
      "text": "Roll about 2 tablespoons of mixture into a 1-inch ball for each meatball",
      "secondary_methods": [
        "MIX"
      ],
      "tools": [
        "spoon",
        "tablespoon"
      ],
      "primary_methods": [],
      "ingredients": []
    },
    {
      "text": "Pour 2 tablespoons olive oil in same skillet used to cook onions",
      "secondary_methods": [],
      "tools": [
        "skillet",
        "spoon",
        "tablespoon"
      ],
      "primary_methods": [],
      "ingredients": [
        "olive oil"
      ]
    },
    {
      "text": "Place skillet over medium heat and brown meatballs on all sides in hot oil, about 5 minutes",
      "secondary_methods": [],
      "tools": [
        "skillet"
      ],
      "primary_methods": [],
      "ingredients": [
        "olive oil"
      ]
    },
    {
      "text": "Hold a crumpled paper towel in a tongs and use it to remove excess grease from skillet",
      "secondary_methods": [],
      "tools": [
        "skillet",
        "tongs"
      ],
      "primary_methods": [],
      "ingredients": []
    },
    {
      "text": "Pour marinara sauce and water over meatballs in skillet",
      "secondary_methods": [],
      "tools": [
        "skillet"
      ],
      "primary_methods": [],
      "ingredients": [
        "marinara sauce",
        "water"
      ]
    },
    {
      "text": "Stir to combine and bring to a simmer",
      "secondary_methods": [],
      "tools": [],
      "primary_methods": [
        "SIMMER",
        "STIR"
      ],
      "ingredients": []
    },
    {
      "text": "Reduce heat to medium-low and simmer, stirring occasionally, until meatballs are cooked through and no longer pink in the center, about 30 minutes",
      "secondary_methods": [
        "REDUCE"
      ],
      "tools": [],
      "primary_methods": [
        "SIMMER",
        "STIR"
      ],
      "ingredients": []
    }
  ],
  "secondary_methods": [
    "MIX",
    "BLEND",
    "REDUCE"
  ],
  "primary_methods": [
    "SAUTE",
    "STIR",
    "SIMMER"
  ],
  "tools": [
    "skillet",
    "spoon",
    "tablespoon",
    "bowl",
    "mixing bowl",
    "tongs"
  ],
  "ingredients": [
    {
      "preparation": "minced",
      "descriptor": "",
      "quantity": "1/2",
      "name": "onion",
      "measurement": ""
    },
    {
      "preparation": "",
      "descriptor": "",
      "quantity": "2",
      "name": "olive oil",
      "measurement": "tablespoons"
    },
    {
      "preparation": "minced",
      "descriptor": "",
      "quantity": "3",
      "name": "cloves garlic",
      "measurement": ""
    },
    {
      "preparation": "ground",
      "descriptor": "",
      "quantity": "1",
      "name": "tofu",
      "measurement": "pound"
    },
    {
      "preparation": "",
      "descriptor": "whole",
      "quantity": "1",
      "name": "milk ricotta cheese",
      "measurement": "cup"
    },
    {
      "preparation": "chopped",
      "descriptor": "Italian packed",
      "quantity": "1/4",
      "name": "parsley",
      "measurement": "cup"
    },
    {
      "preparation": "beaten",
      "descriptor": "",
      "quantity": "1",
      "name": "egg",
      "measurement": ""
    },
    {
      "preparation": "",
      "descriptor": "",
      "quantity": "1 1/2",
      "name": "kosher salt",
      "measurement": "teaspoons"
    },
    {
      "preparation": "freshly ground",
      "descriptor": "",
      "quantity": "1/2",
      "name": "black pepper",
      "measurement": "teaspoon"
    },
    {
      "preparation": "or to taste",
      "descriptor": "",
      "quantity": "1",
      "name": "cayenne pepper",
      "measurement": "pinch"
    },
    {
      "preparation": "dry",
      "descriptor": "",
      "quantity": "1/3",
      "name": "bread crumbs",
      "measurement": "cup"
    },
    {
      "preparation": "",
      "descriptor": "",
      "quantity": "2",
      "name": "olive oil",
      "measurement": "tablespoons"
    },
    {
      "preparation": "",
      "descriptor": "jar",
      "quantity": "1",
      "name": "marinara sauce",
      "measurement": "28 ounce"
    },
    {
      "preparation": "",
      "descriptor": "",
      "quantity": "1",
      "name": "water",
      "measurement": "cup"
    }
  ]
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
					new_recipe['steps'][i]['text'] = new_recipe['steps'][i]['text'].replace(key, meat2veg[key])

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
					new_recipe['steps'][i]['text'] = new_recipe['steps'][i]['text'].replace(key, veg2meat[key])

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
						new_recipe['steps'][i]['text'] = new_recipe['steps'][i]['text'].replace(key, d[key])

	# replace methods
	d = to_healthy_methods
	for key in to_healthy_methods:
		# update list of methods
		for i, method in enumerate(new_recipe['primary_methods']):
			method = method.lower()
			if key in method:
				new_recipe['primary_methods'][i] = method.replace(key, d[key])
		for i, method in enumerate(new_recipe['secondary_methods']):
			method = method.lower()
			if key in method:
				new_recipe['secondary_methods'][i] = method.replace(key, d[key])

		# update method in list of steps
		for i, step in enumerate(new_recipe['steps']):
			primary_methods = step['primary_methods']
			for j, method_name in enumerate(primary_methods):
				method_name = method_name.lower()
				#iterate thru keys in the dictionary. if key a substring in method name, replace method name w value
				for key in d:
					if key in method_name:
						new_recipe['steps'][i]['primary_methods'][j] = method_name.replace(key, d[key])
						new_recipe['steps'][i]['text'] = new_recipe['steps'][i]['text'].replace(key, d[key])

			secondary_methods = step['secondary_methods']
			for j, method_name in enumerate(secondary_methods):
				method_name = method_name.lower()
				#iterate thru keys in the dictionary. if key a substring in method name, replace method name w value
				for key in d:
					if key in method_name:
						new_recipe['steps'][i]['secondary_methods'][j] = method_name.replace(key, d[key])
						new_recipe['steps'][i]['text'] = new_recipe['steps'][i]['text'].replace(key, d[key])

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
		for i, method in enumerate(step['primary_methods']):
			method = method.lower()
			if method == oldm:
				step['primary_methods'][i] = newm
				step["text"] =  step["text"].replace(oldm, newm)
		for i, method in enumerate(step['secondary_methods']):
			method = method.lower()
			if method == oldm:
				step['secondary_methods'][i] = newm
				step["text"] =  step["text"].replace(oldm, newm)
	# replace method in list of methods
	for i, method in enumerate(myrec["primary_methods"]):
		if method.lower() == oldm.lower():
			myrec['primary_methods'][i] = newm
	for i, method in enumerate(myrec["secondary_methods"]):
		if method.lower() == oldm.lower():
			myrec['secondary_methods'][i] = newm

	return myrec

# ------------------------------------------------------------------------------------------------------------------------

#test
# print '\n******************** Meat 2 Vegetarian transformation ************************\n'
# print json.dumps(transform_to_vegetarian(parsed_vals), sort_keys=True, indent=2)
# print '\n******************** Vegetarian 2 Meat transformation ************************\n'
# print json.dumps(transform_from_vegetarian(parsed_vals), sort_keys=True, indent=2)
# print '\n************************ Healthy transformation ****************************\n'
# print json.dumps(transform_to_healthy(parsed_vals), sort_keys=True, indent=2)
# print '\n************************ Replace cooking method transformations ****************\n'
# print json.dumps(replace_methods(parsed_vals), sort_keys=True, indent=2)