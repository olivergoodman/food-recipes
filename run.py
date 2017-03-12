from recipce_parser import main
from transformations import transform_to_vegetarian, transform_from_vegetarian, transform_to_healthy, replace_methods
import json

recipe_url = 'http://allrecipes.com/recipe/235710/chef-johns-ricotta-meatballs/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=235710&referringContentType=recipe'



if __name__ == "__main__":
	recipe = main(recipe_url)
	print type(recipe)
	try:
		transformation_num = int(raw_input('Select a transformation:\n\t(1)To Vegetarian\n\t(2)From Vegetarian\n\t(3)To Healthy\n\t(4)Replace Methods\nPlease input a number:\t'))
	except:
		print "Need to input a number that corresponds to a transformation"

	if transformation_num == 1:
		print json.dumps(transform_to_vegetarian(recipe), indent=2)

	elif transformation_num == 2:
		print json.dumps(transform_from_vegetarian(recipe), indent=2)

	elif transformation_num == 3:
		print json.dumps(transform_to_healthy(recipe), indent=2)

	elif transformation_num == 4:
		print json.dumps(replace_methods(recipe), indent=2)

