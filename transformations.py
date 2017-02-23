# plan of action

# transformations:
# 	- to/from vegetarian
# 	- to/from healthy
# 	- cooking method (ex. from bake to stir-fry)

# veggie sub:
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

	direction = direction.replace(replace_this['name'], tofu['name'])

	return direction, tofu


# to/from health transformation
healthy_fats = ['olive oil', 'sunflower oil', 'coconut oil']
unhealthy_fats = ['butter', 'lard', 'shortening', 'canola oil', 'margarine']
healthy_protein = ['ground beef', 'pork', 'lamb', ]
unhealthy_protein = ['liver', 'tofu', 'chicken', 'turkey']
healthy_dairy = ['milk, yogurt']
unhealthy_dairy = ['butter', 'cheese', 'whipped cream']
healthy_salts = ['low-sodium soy sauce', 'table salt']
unhealthy_salts = ['soy sauce', 'sea salt']
healthy_grains = ['rice', 'pasta']
unhealthy_grains = ['brown rice', 'whole wheat pasta']
healthy_sugars = ['honey', 'maple syrup', 'agave', 'coconut sugar', 'date sugar']
unhealthy_sugars = ['sugar', 'brown sugar', 'confectioners sugar', 'caramel', 'chocolate syrup']



#test 
str = "Fry chicken in oil. Then sprinkle with salt."
chicken = {
			'name': 'chicken',
			'quantity': 1,
			'measurement': 'pound'
			}


new_direction, tofu = subsitute_meat_for_veg(str, chicken)
print new_direction, tofu