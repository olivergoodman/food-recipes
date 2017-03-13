from recipce_parser import main
from transformations import transform_to_vegetarian, transform_from_vegetarian, transform_to_healthy, replace_methods
from coding_util import print_recipe_readable
import json

### ricotta meatballs: http://allrecipes.com/recipe/235710/chef-johns-ricotta-meatballs/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=235710&referringContentType=recipe
### sausage_casserole: http://allrecipes.com/recipe/241105/sausage-hash-brown-breakfast-casserole/?clickId=right%20rail%202&internalSource=rr_feed_recipe&referringId=241105&referringContentType=recipe
### house chick fried rice: http://allrecipes.com/recipe/18294/house-fried-rice/

if __name__ == "__main__":
	recipe_url = raw_input('Paste the url of the recipe here:\t')
	recipe = main(recipe_url)
	try:
		transformation_num = int(raw_input('\nSelect a transformation:\n\t(1) Original Recipe\n\t(2) To Vegetarian\n\t(3) From Vegetarian\n\t(4) To Healthy\n\t(5) Replace Methods\nPlease input a number:\t'))
		format_num = int(raw_input('\nSelect a view format:\n\t(1) Clean view\n\t(2) JSON view\nPlease input a number:\t'))
		print '\n\n------ Recipe ------\n'
	except:
		print "Need to input a number that corresponds to a transformation"

	if transformation_num == 1:
		if format_num == 1:
			print_recipe_readable(recipe)
		elif format_num == 2:
			print json.dumps(recipe, indent=2)

	elif transformation_num == 2:
		new_recipe = transform_to_vegetarian(recipe)
		if format_num == 1:
			print_recipe_readable(new_recipe)
		elif format_num == 2:
			print json.dumps(transform_to_vegetarian(recipe), indent=2)

	elif transformation_num == 3:
		new_recipe = transform_from_vegetarian(recipe)
		if format_num == 1:
			print_recipe_readable(new_recipe)
		elif format_num == 2:
			print json.dumps(transform_from_vegetarian(recipe), indent=2)

	elif transformation_num == 4:
		new_recipe = transform_to_healthy(recipe)
		if format_num == 1:
			print_recipe_readable(new_recipe)
		elif format_num == 2:
			print json.dumps(transform_to_healthy(recipe), indent=2)


	elif transformation_num == 5:
		print 'Methods are: ' + ' '.join(recipe['primary_methods'] + recipe['secondary_methods'])
		new_recipe = replace_methods(recipe)

		if format_num == 1:
			print_recipe_readable(new_recipe)
		elif format_num == 2:
			print json.dumps(replace_methods(recipe), indent=2)

