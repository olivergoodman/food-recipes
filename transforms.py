from veggies import meat2veg

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


to_healthy_fats = {
	'butter': 'olive oil', 
	'lard': 'olive oil', 
	'shortening': 'olive oil', 
	'canola oil': 'olive oil', 
	'margarine': 'olive oil',  
	'coconut oil': 'avocado oil',  
	'tallow': 'soybean oil',   
	'palm oil': 'sunflower oil',  
	'palm kemel oil': 'sunflower oil',  
	'chicken fat': 'olive oil',  
	'hydrogenated oils': 'non-hydrogenated oils'
}

to_healthy_protein = meat2veg

to_healthy_dairy = {
	'reduced-fat milk': 'fat free milk', 
	'cream cheese': 'low fat cream cheese', 
	'whole milk' : 'fat free milk', 
	'butter': 'olive oil', 
	'cheese': 'low fat cheese', 
	'whipped cream': 'fat free yogurt',  
	'sour cream': 'fat free yogurt'
}

to_healthy_salts = {
	'soy sauce': 'low sodium soy sauce', 
	'table salt': 'sea salt',
	'salt': 'sea salt'
}

to_healthy_grains = {
	'macaroni': 'whole wheat macaroni', 
	'noodles': 'buckwheat spaghetti', 
	'spaghetti': 'whole wheat spaghetti', 
	'white rice': 'brown rice', 
	'rice': 'brown rice',
	'bread': 'whole wheat bread', 
	'pasta': 'whole wheat pasta'
}

to_healthy_sugars = {
	'sugar': 'cane sugar',
	'brown sugar': 'maple syrup',
	'white sugar': 'cane sugar', 
	'corn syrup': 'maple syrup', 
	'chocolate syrup': 'honey',
	'chocolate': 'organic dark chocolate',
	'caramel': 'maple syrup'
}

to_healthy_methods = {
	'fry' : 'stir fry',
	'deep fry': 'stir fry',
	'grill' : 'steam',
	'barbeque' : 'bake',
	'roast' : 'bake',
}

