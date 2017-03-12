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
      "tools": [
        "skillet",
        "spoon",
        "tablespoon"
      ],
      "method": [
        "SAUTE"
      ],
      "ingredients": [
        "onion",
        "olive oil",
        "olive oil"
      ]
    },
    {
      "text": "Stir garlic into onion and turn off heat",
      "tools": [],
      "method": [
        "STIR"
      ],
      "ingredients": [
        "onion"
      ]
    },
    {
      "text": "Transfer onion mixture to a large mixing bowl",
      "tools": [
        "bowl",
        "mixing bowl"
      ],
      "method": [
        "MIX"
      ],
      "ingredients": [
        "onion"
      ]
    },
    {
      "text": "Stir ground beef, ricotta cheese, parsley, egg, kosher salt, black pepper, and cayenne pepper with onion mixture until almost combined; stir in bread crumbs and continue to mix until thoroughly blended",
      "tools": [],
      "method": [
        "BLEND",
        "MIX",
        "STIR"
      ],
      "ingredients": [
        "onion",
        "beef",
        "ricotta cheese",
        "parsley",
        "egg",
        "kosher salt",
        "black pepper",
        "cayenne pepper",
        "bread crumbs"
      ]
    },
    {
      "text": "Roll about 2 tablespoons of mixture into a 1-inch ball for each meatball",
      "tools": [
        "spoon",
        "tablespoon"
      ],
      "method": [
        "MIX"
      ],
      "ingredients": []
    },
    {
      "text": "Pour 2 tablespoons olive oil in same skillet used to cook onions",
      "tools": [
        "skillet",
        "spoon",
        "tablespoon"
      ],
      "method": [],
      "ingredients": [
        "onion",
        "olive oil",
        "olive oil"
      ]
    },
    {
      "text": "Place skillet over medium heat and brown meatballs on all sides in hot oil, about 5 minutes",
      "tools": [
        "skillet"
      ],
      "method": [],
      "ingredients": []
    },
    {
      "text": "Hold a crumpled paper towel in a tongs and use it to remove excess grease from skillet",
      "tools": [
        "skillet",
        "tongs"
      ],
      "method": [],
      "ingredients": []
    },
    {
      "text": "Pour marinara sauce and water over meatballs in skillet",
      "tools": [
        "skillet"
      ],
      "method": [],
      "ingredients": [
        "marinara sauce",
        "water"
      ]
    },
    {
      "text": "Stir to combine and bring to a simmer",
      "tools": [],
      "method": [
        "SIMMER",
        "STIR"
      ],
      "ingredients": []
    },
    {
      "text": "Reduce heat to medium-low and simmer, stirring occasionally, until meatballs are cooked through and no longer pink in the center, about 30 minutes",
      "tools": [],
      "method": [
        "REDUCE",
        "SIMMER",
        "STIR"
      ],
      "ingredients": []
    }
  ],
  "tools": [
    "skillet",
    "spoon",
    "tablespoon",
    "bowl",
    "mixing bowl",
    "tongs"
  ],
  "methods": [
    "SAUTE",
    "STIR",
    "MIX",
    "BLEND",
    "SIMMER",
    "REDUCE"
  ],
  "ingredients": [
    {
      "preparation": "",
      "descriptor": "minced",
      "measurement": "",
      "name": "onion",
      "quantity": "1/2"
    },
    {
      "preparation": "",
      "descriptor": "",
      "measurement": "tablespoons",
      "name": "olive oil",
      "quantity": "2"
    },
    {
      "preparation": "",
      "descriptor": "minced",
      "measurement": "",
      "name": "cloves garlic",
      "quantity": "3"
    },
    {
      "preparation": "",
      "descriptor": "ground",
      "measurement": "pound",
      "name": "beef",
      "quantity": "1"
    },
    {
      "preparation": "",
      "descriptor": "whole milk",
      "measurement": "cup",
      "name": "ricotta cheese",
      "quantity": "1"
    },
    {
      "preparation": "",
      "descriptor": "packed chopped Italian",
      "measurement": "cup",
      "name": "parsley",
      "quantity": "1/4"
    },
    {
      "preparation": "",
      "descriptor": "beaten",
      "measurement": "",
      "name": "egg",
      "quantity": "1"
    },
    {
      "preparation": "",
      "descriptor": "",
      "measurement": "teaspoons",
      "name": "kosher salt",
      "quantity": "1 1/2"
    },
    {
      "preparation": "",
      "descriptor": "freshly ground",
      "measurement": "teaspoon",
      "name": "black pepper",
      "quantity": "1/2"
    },
    {
      "preparation": "",
      "descriptor": "or to taste",
      "measurement": "pinch",
      "name": "cayenne pepper",
      "quantity": "1"
    },
    {
      "preparation": "",
      "descriptor": "dry",
      "measurement": "cup",
      "name": "bread crumbs",
      "quantity": "1/3"
    },
    {
      "preparation": "",
      "descriptor": "",
      "measurement": "tablespoons",
      "name": "olive oil",
      "quantity": "2"
    },
    {
      "preparation": "",
      "descriptor": "jar",
      "measurement": "28 ounce",
      "name": "marinara sauce",
      "quantity": "1"
    },
    {
      "preparation": "",
      "descriptor": "",
      "measurement": "cup",
      "name": "water",
      "quantity": "1"
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