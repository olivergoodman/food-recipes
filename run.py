from recipce_parser import main
from transformations import transform_to_vegetarian, transform_from_vegetarian, transform_to_healthy, replace_methods
from coding_util import print_recipe_readable
import json

# recipe_url = 'http://allrecipes.com/recipe/235710/chef-johns-ricotta-meatballs/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=235710&referringContentType=recipe'
sausage_casserole= 'http://allrecipes.com/recipe/241105/sausage-hash-brown-breakfast-casserole/?clickId=right%20rail%202&internalSource=rr_feed_recipe&referringId=241105&referringContentType=recipe'


if __name__ == "__main__":
	recipe_url = raw_input('Paste the url of the recipe here:\t')
	recipe = main(recipe_url)
	try:
		transformation_num = int(raw_input('\nSelect a transformation:\n\t(0) Original Recipe\n\t(1) To Vegetarian\n\t(2) From Vegetarian\n\t(3) To Healthy\n\t(4) Replace Methods\nPlease input a number:\t'))
		print '\n\n------ Recipe ------\n'
	except:
		print "Need to input a number that corresponds to a transformation"

	if transformation_num == 0:
		print_recipe_readable(recipe)

	elif transformation_num == 1:
		# print json.dumps(transform_to_vegetarian(recipe), indent=2)
		new_recipe = transform_to_vegetarian(recipe)
		print_recipe_readable(new_recipe)

	elif transformation_num == 2:
		# print json.dumps(transform_from_vegetarian(recipe), indent=2)
		new_recipe = transform_from_vegetarian(recipe)
		print_recipe_readable(new_recipe)

	elif transformation_num == 3:
		# print json.dumps(transform_to_healthy(recipe), indent=2)
		new_recipe = transform_to_healthy(recipe)
		print_recipe_readable(new_recipe)

	elif transformation_num == 4:
		# print json.dumps(replace_methods(recipe), indent=2)
		new_recipe = replace_methods(recipe)
		print_recipe_readable(new_recipe)

