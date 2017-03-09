# transformations:
# 	- to/from vegetarian
# 	- to/from healthy
# 	- cooking method (ex. from bake to stir-fry)
import re
import random
import copy
from veggies import veg2meat, meat2veg
from transforms import healthy_fats, unhealthy_fats, unhealthy_protein, healthy_protein, unhealthy_dairy, healthy_dairy, unhealthy_salts, healthy_salts, unhealthy_grains, healthy_grains, unhealthy_sugars, healthy_sugars, unhealthy_methods, healthy_methods
# NOTE: tranformations should change both the list of ingredients and the ingredients inside steps
#	return format: 
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
			"name": "chicken",
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
# # veggie sub:
# meats = ['chicken', 'beef', 'turkey', 'pork', 'venison']

# # should take in the steps -- broken up by sentence in directions
# def subsitute_meat_for_veg(direction, replace_this):
# 	"""
# 	given a direction (string) and meat object to replace,
# 	returns direction with tofu subsituted and new tofu ingredient object
# 	"""

# 	tofu = {
# 			'name': 'tofu',
# 			'quantity': replace_this['quantity'],
# 			'measurement': replace_this['measurement']
# 			}
# 	for meat in meats:
# 		if meat in direction:
# 			direction = direction.replace(replace_this['name'], tofu['name'])

# 	return direction, tofu


# veggie sub:
meats = ['chicken', 'beef', 'turkey', 'pork', 'venison', 'salmon', 'tuna', 'halibut', '']

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
		print step, i



	# for meat in meats:
	# 	if meat in direction:
	# 		direction = direction.replace(replace_this['name'], tofu['name'])

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
	oldm = raw_input('what method do you want to change?    ')
	newm = raw_input ('what do you want to change it into?    ')
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
print replace_methods(parsed_vals)
print '\n********\n'

