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

healthy_fats = ['olive oil', 'sunflower oil', 'soybean oil', 'corn oil',  'sesame oil',  'peanut oil']
unhealthy_fats = ['butter', 'lard', 'shortening', 'canola oil', 'margarine',  'coconut oil',  'tallow',  'cream',   'milk fat',  'palm oil',  'palm kemel oil',  'chicken fat',  'hydrogenated oils']
healthy_protein = [ 'peas',  'beans', 'eggs', 'crab', 'fish','chicken', 'tofu', 'ground beef', 'turkey']
unhealthy_protein = ['liver', 'beef', 'pork', 'lamb']
healthy_dairy = [ 'fat-free milk', 'low-fat milk, ‘yogurt',  'low fat cheese']
unhealthy_dairy = [ 'reduced-fat milk', 'cream cheese', 'whole milk', 'butter', 'cheese', 'whipped cream',  'sour cream']
healthy_salts = ['low-sodium soy sauce', 'sea salt', 'kosher salt']
unhealthy_salts = ['soy sauce', 'table salt']
healthy_grains = ['oat cereal', 'wild rice', 'oatmeal', 'whole rye', 'buckwheat', 'rolled oats', 'quinoa','bulgur', 'millet', 'brown rice', 'whole wheat pasta']
unhealthy_grains = ['macaroni', 'noodles', 'spaghetti', 'white rice', 'white bread', 'regular white pasta']
healthy_sugars = ['real fruit jam', 'fruit juice concentrates', 'monk fruit extract', 'cane sugar', 'molasses', 'brown rice syrup' 'stevia', 'honey', 'maple syrup', 'agave syrup', 'coconut sugar', 'date sugar', 'sugar alcohols', 'brown sugar']
unhealthy_sugars = ['aspartame', 'acesulfame K', 'sucralose', 'white sugar', 'corn syrup', 'chocolate syrup']

#test
str = "Fry chicken in oil. Then sprinkle with salt."
chicken = {
			'name': 'chicken',
			'quantity': 1,
			'measurement': 'pound'
			}


new_direction, tofu = subsitute_meat_for_veg(str, chicken)
print new_direction, tofu
