# transformations:
# 	- to/from vegetarian
# 	- to/from healthy
# 	- cooking method (ex. from bake to stir-fry)
import re
import random
import copy
import json
from veggies import veg2meat, meat2veg
# NOTE: tranformations should change both the list of ingredients and the ingredients inside steps
#	return format: 
parsed_vals = {
	"tools": ["", ""],
	"methods": ["", ""],
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
			"method": "chop",
			"ingredients": ['garlic', 'chicken'],
			"tools": ["knife","spoon"], 
			"text": ""
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

healthy_fats = ['olive oil', 'sunflower oil', 'soybean oil', 'corn oil',  'sesame oil',  'peanut oil']
unhealthy_fats = ['butter', 'lard', 'shortening', 'canola oil', 'margarine',  'coconut oil',  'tallow',  'cream',   'milk fat',  'palm oil',  'palm kemel oil',  'chicken fat',  'hydrogenated oils']
healthy_protein = [ 'peas',  'beans', 'eggs', 'crab', 'fish','chicken', 'tofu', 'liver', 'turkey']
unhealthy_protein = ['ground beef', 'beef', 'pork', 'lamb']
healthy_dairy = [ 'fat free milk', 'low fat milk', 'yogurt',  'low fat cheese']
unhealthy_dairy = [ 'reduced-fat milk', 'cream cheese', 'whole milk', 'butter', 'cheese', 'whipped cream',  'sour cream']
healthy_salts = ['low sodium soy sauce', 'sea salt', 'kosher salt']
unhealthy_salts = ['soy sauce', 'table salt','salt']
healthy_grains = ['oat cereal', 'wild rice', 'oatmeal', 'whole rye', 'buckwheat', 'rolled oats', 'quinoa','bulgur', 'millet', 'brown rice', 'whole wheat pasta']
unhealthy_grains = ['macaroni', 'noodles', 'spaghetti', 'white rice', 'white bread', 'regular white pasta']
healthy_sugars = ['real fruit jam', 'fruit juice concentrates', 'monk fruit extract', 'cane sugar', 'molasses', 'brown rice syrup' 'stevia', 'honey', 'maple syrup', 'agave syrup', 'coconut sugar', 'date sugar', 'sugar alcohols', 'brown sugar']
unhealthy_sugars = ['aspartame', 'acesulfame K', 'sucralose', 'white sugar', 'corn syrup', 'chocolate syrup']
healthy_methods = ["boil"]
unhealthy_methods = ["fry"]

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

	
	print(vals["steps"][0]["text"])
	print(myrec["steps"][0]["text"])
	print(vals["steps"][0]["ingredients"])
	print(myrec["steps"][0]["ingredients"])
	print(vals["steps"][1]["text"])
	print(myrec["steps"][1]["text"])
	print(vals["steps"][1]["ingredients"])
	print(myrec["steps"][1]["ingredients"])
	print(vals["methods"])
	print(myrec["methods"])

	return myrec

def replace_methods(vals):
# takes in vals, oldm, newm

	oldm = raw_input('What cooking method do you want to replace? ')
	newm = raw_input('What is the new cooking method? ')

	myrec = copy.deepcopy(vals)
	for each in myrec["steps"]:
		if each["method"] == oldm:
			each["method"] = newm
			each["text"] =  each["text"].replace(oldm, newm)
	for each in myrec["methods"]:
		if each == oldm:
			myrec["methods"].remove(oldm)
			myrec["methods"].append(newm)
	print(vals["methods"])
	print(myrec["methods"])
	print(vals["steps"][1]["text"])
	print(myrec["steps"][1]["text"])
	return myrec

# ------------------------------------------------------------------------------------------------------------------------

#test
print '**** Meat 2 Vegetarian transformation ****\n'
print json.dumps(transform_to_vegetarian(parsed_vals), 2)

print '\n**** Veggie 2 Meat transformation ****\n'
print json.dumps(transform_from_vegetarian(parsed_vals), 2)


print '\n********\n'

replace_methods(parsed_vals)