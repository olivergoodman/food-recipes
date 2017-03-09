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
			"measurement": "",
			"name": "clove garlic",
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
			"name": "tofu",
			"quantity": "1"
	    }],
	"steps": [ 
		{
			"method": "grill",
			"ingredients": ['garlic', 'chicken'],
			"tools": ["knife","spoon"], 
			"text": "grill chicken and then put some garlic on top"
		},
		{
			"method": "",
			"ingredients": ['beans', 'potatos'],
			"tools": [], 
			"text": "test text"
		}]
}


# ------------------------------------------------------------------------------------------------------------------------
# veggie sub:

# should take in the steps -- broken up by sentence in directions
def transform_to_vegetarian(recipe):
	"""
	given a recipe (in JSON format above),
	returns recipe JSON with both list of ingredients and ingredients in steps changed
	"""

	new_recipe = copy.deepcopy(recipe)

	# update list of ingredients
	for i, ingredient in enumerate(new_recipe['ingredients']):
		name = ingredient['name']
		if name in meat2veg:
			new_recipe['ingredients'][i]['name'] = meat2veg[name]

	# update list of ingredients in steps
	for i, step in enumerate(new_recipe['steps']):
		ingredients = step['ingredients']
		for j, ingredient_name in enumerate(ingredients):
			if ingredient_name in meat2veg:
				ingredients[j] = meat2veg[ingredient_name]

	return new_recipe


def transform_from_vegetarian(recipe):
	"""
	given a vegetarian recipe (in JSON format above),
	returns recipe JSON with both list of ingredients and ingredients in steps changed
	"""

	new_recipe = copy.deepcopy(recipe)

	# update list of ingredients
	for i, ingredient in enumerate(new_recipe['ingredients']):
		name = ingredient['name']
		if name in veg2meat:
			new_recipe['ingredients'][i]['name'] = veg2meat[name]

	# update list of ingredients in steps
	for i, step in enumerate(new_recipe['steps']):
		ingredients = step['ingredients']
		for j, ingredient_name in enumerate(ingredients):
			if ingredient_name in veg2meat:
				ingredients[j] = veg2meat[ingredient_name]

	return new_recipe

# ------------------------------------------------------------------------------------------------------------------------
# to/from health transformation

# print return_val["steps"][1]["text"]
def transform_to_healthy(vals):
	myrec = copy.deepcopy(vals)
	for each in myrec["ingredients"]:
		if each["name"] in unhealthy_protein:
			mytemp = each["name"]
			mylength = len(healthy_protein)-1
			mikoto = random.randint(0,mylength)
			each["name"] = healthy_protein[mikoto]
			for modtext in myrec["steps"]:
				modtext["text"] = modtext["text"].replace(mytemp, each["name"])
				if mytemp in modtext["ingredients"]:
					modtext["ingredients"].remove(mytemp)
					modtext["ingredients"].append(each["name"])

		if each["name"] in unhealthy_fats:
			mytemp = each["name"]
			mylength = len(healthy_protein)-1
			mikoto = random.randint(0,mylength)
			each["name"] = healthy_protein[mikoto]
			each["name"] = healthy_fats[mikoto]
			for modtext in myrec["steps"]:
				modtext["text"] = modtext["text"].replace(mytemp, each["name"])
				if mytemp in modtext["ingredients"]:
					modtext["ingredients"].remove(mytemp)
					modtext["ingredients"].append(each["name"])

		if each["name"] in unhealthy_dairy:
			mytemp = each["name"]
			mylength = len(healthy_protein)-1
			mikoto = random.randint(0,mylength)
			each["name"] = healthy_protein[mikoto]
			each["name"] = healthy_dairy[mikoto]
			for modtext in myrec["steps"]:
				modtext["text"] = modtext["text"].replace(mytemp, each["name"])
				if mytemp in modtext["ingredients"]:
					modtext["ingredients"].remove(mytemp)
					modtext["ingredients"].append(each["name"])

		if each["name"] in unhealthy_salts:
			mytemp = each["name"]
			mylength = len(healthy_protein)-1
			mikoto = random.randint(0,mylength)
			each["name"] = healthy_protein[mikoto]
			each["name"] = healthy_salts[mikoto]
			for modtext in myrec["steps"]:
				modtext["text"] = modtext["text"].replace(mytemp, each["name"])
				if mytemp in modtext["ingredients"]:
					modtext["ingredients"].remove(mytemp)
					modtext["ingredients"].append(each["name"])

		if each["name"] in unhealthy_grains:
			mytemp = each["name"]
			mylength = len(healthy_protein)-1
			mikoto = random.randint(0,mylength)
			each["name"] = healthy_protein[mikoto]
			each["name"] = healthy_grains[mikoto]
			for modtext in myrec["steps"]:
				modtext["text"] = modtext["text"].replace(mytemp, each["name"])
				if mytemp in modtext["ingredients"]:
					modtext["ingredients"].remove(mytemp)
					modtext["ingredients"].append(each["name"])

		if each["name"] in unhealthy_sugars:
			mytemp = each["name"]
			mylength = len(healthy_protein)-1
			mikoto = random.randint(0,mylength)
			each["name"] = healthy_protein[mikoto]
			each["name"] = healthy_sugars[mikoto]
			for modtext in myrec["steps"]:
				modtext["text"] = modtext["text"].replace(mytemp, each["name"])
				if mytemp in modtext["ingredients"]:
					modtext["ingredients"].remove(mytemp)
					modtext["ingredients"].append(each["name"])

	for each in myrec["steps"]:
		if each["method"] in unhealthy_methods:
			tempmeth = each["method"]
			mylen = len(healthy_methods)-1
			kuroko = random.randint(0,mylen)
			each["method"] = healthy_methods[kuroko]
			each["text"] =  each["text"].replace(tempmeth, each["method"])
			for mymeths in myrec["methods"]:
				if mymeths == tempmeth:
					myrec["methods"].remove(tempmeth)
					myrec["methods"].append(each["method"])
	return myrec

def replace_methods(vals):
# takes in vals, oldm, newm
	oldm = raw_input('What cooking method do you want to change?    ')
	newm = raw_input ('What do you want to change it into?    ')
	myrec = copy.deepcopy(vals)
	for each in myrec["steps"]:
		if each["method"] == oldm:
			each["method"] = newm
			each["text"] =  each["text"].replace(oldm, newm)
	for each in myrec["methods"]:
		if each == oldm:
			myrec["methods"].remove(oldm)
			myrec["methods"].append(newm)

	return myrec

# ------------------------------------------------------------------------------------------------------------------------

#test
print '\n**** Meat 2 Vegetarian transformation ****\n'
print transform_to_vegetarian(parsed_vals)
print '\n**** Vegetarian 2 Meat transformation ****\n'
print transform_to_vegetarian(parsed_vals)
print '\n**** Healthy transformation ****\n'
print transform_to_healthy(parsed_vals)
print '\n**** Replace cooking method transformations ****\n'
print replace_methods(parsed_vals)