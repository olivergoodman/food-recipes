# transformations:
# 	- to/from vegetarian
# 	- to/from healthy
# 	- cooking method (ex. from bake to stir-fry)
import re
import random
import copy
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
	    }],
	"steps": [ 
		{
			"method": "",
			"ingredients": [],
			"tools": ["",""], 
			"text": ""
		},
		{
			"method": "",
			"ingredients": [],
			"tools": [], 
			"text": "test text"
		}]
}


# ------------------------------------------------------------------------------------------------------------------------

# veggie sub:
meats = ['chicken', 'beef', 'turkey', 'pork', 'venison']

# should take in the steps -- broken up by sentence in directions
def subsitute_meat_for_veg(direction, replace_this):
	"""
	given a direction (string) and meat object to replace,
	returns direction with tofu subsituted and new tofu ingredient object
	"""

	tofu = {
			'name': 'tofu',
			'quantity': replace_this['quantity'],
			'measurement': replace_this['measurement']
			}
	for meat in meats:
		if meat in direction:
			direction = direction.replace(replace_this['name'], tofu['name'])

	return direction, tofu



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
healthy_methods = []
unhealthy_methods = ["fry"]

# print return_val["steps"][1]["text"]
def transform_to_healthy():
	vals = {
	"tools": ["", ""],
	"methods": ["", ""],
	"ingredients": [
	    {
			"preparation": "",
			"descriptor": "",
			"measurement": "pound",
			"name": "beef",
			"quantity": "1"
	    },
	    {
			"preparation": "",
			"descriptor": "",
			"measurement": "pack",
			"name": "spaghetti",
			"quantity": "1"
	    }],
	"steps": [ 
		{
			"method": "",
			"ingredients": ["spaghetti"],
			"tools": ["",""], 
			"text": "boil spaghetti until it turns soft"
		},
		{
			"method": "",
			"ingredients": ["beef"],
			"tools": [], 
			"text": "cook beef in pan"
		}]
}
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

	#myrec["steps"][1]["text"] = "ayyylmao"
	print(vals["steps"][1]["text"])
	print(myrec["steps"][1]["text"])
	print(vals["steps"][1]["ingredients"])
	print(myrec["steps"][1]["ingredients"])

	return 


# ------------------------------------------------------------------------------------------------------------------------

#test
transform_to_healthy()
str = "Fry chicken in oil. Then sprinkle with salt."
chicken = {
			'name': 'chicken',
			'quantity': 10,
			'measurement': 'ounces'
			}


new_direction, tofu = subsitute_meat_for_veg(str, chicken)
#print new_direction, tofu
