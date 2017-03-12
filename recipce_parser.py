__author__ = 'cmark'
from bs4 import BeautifulSoup
import urllib2
import json
import re
import string
import coding_util as cu

# test urls
recipe_url = 'http://allrecipes.com/recipe/235710/chef-johns-ricotta-meatballs/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=235710&referringContentType=recipe'
rec = 'http://allrecipes.com/recipe/191793/country-fried-steak/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%201'
rec2 = 'http://allrecipes.com/recipe/241105/sausage-hash-brown-breakfast-casserole/?clickId=right%20rail%202&internalSource=rr_feed_recipe&referringId=241105&referringContentType=recipe'
# probably a better way to do this and be able to exclude plurals
measurements = ['cup', 'cups', 'teaspoon', 'teaspoons', 'tablespoon','tablespoons','quart','quarts','gallon', 'gallons',
                'litre','litres', 'pint', 'pints', 'pinch', 'pinches', 'pound', 'pounds', 'ounce', 'ounces' 'fluid ounce', 'fluid ounces']

# cooking_method_terms
cooking_methods = ['AL DENTE', 'BAKE', 'BARBECUE', 'BASTE', 'BATTER', 'BEAT', 'BLANCH', 
'BLEND', 'BOIL', 'BROIL', 'CARAMELIZE', 'CHOP', 'CLARIFY', 'CREAM', 'CURE', 'DEGLAZE',
 'DEGREASE', 'DICE', 'DISSOLVE', 'DREDGE', 'DRIZZLE', 'DUST', 'FILLET', 'FLAKE', 
 'FLAMBE', 'FOLD', 'FRICASSEE', 'FRY', 'GARNISH', 'GLAZE', 'GRATE', 'GRATIN', 'GRILL', 
 'GRIND', 'JULIENNE', 'KNEAD', 'LUKEWARM', 'MARINATE', 'MEUNIERE', 'MINCE', 'MIX', 
 'PAN-BROIL', 'PAN-FRY', 'PARBOIL', 'PARE', 'PEEL', 'PICKLE', 'PINCH', 'PIT', 'PLANKED', 
 'PLUMP', 'POACH', 'PUREE', 'REDUCE', 'REFRESH', 'RENDER', 'ROAST', 'SAUTE', 'SCALD', 
 'SCALLOP', 'SCORE', 'SEAR', 'SHRED', 'SIFT', 'SIMMER', 'SKIM', 'STEAM', 'STEEP', 
 'STERILIZE', 'STEW', 'STIR', 'TOSS', 'TRUSS', 'WHIP', 'WHISK']

# simple cooking tool terms
cooking_tools_one = ['apron', 'baster', 'blender', 'bowl', 'carafe', 'colander', 'cookbook',
'corer', 'crock', 'cutlery', 'fork', 'grater', 'griddle', 'grinder', 'infuser', 
'juicer', 'kettle', 'knife', 'ladle', 'lid', 'mandolin', 'mold', 'oven', 'pan', 
'peeler', 'percolator', 'pitcher', 'platter', 'poacher', 'pot', 'ramekin', 
'refrigerator', 'ricer', 'roaster', 'scissors', 'shears', 'sieve', 'skewer', 'skillet', 
'slicer', 'spoon', 'steamer', 'stockpot', 'stove', 'strainer', 'tablespoon', 'teakettle', 
'teaspoon', 'thermometer', 'toaster', 'tongs', 'trivet', 'utensils', 'whisk', 'wok', 
'zester']

# complex cooking tool terms
cooking_tools_two = ['baking sheet', 'barbecue grill', 'basting brush', 'bread basket', 
'butcher block', 'can opener', 'charcoal grill', 'cheese cloth', 'coffee maker', 
'cookie cutter', 'cookie press', 'cookie sheet', 'cooling rack', 'custard cup', 
'cutting board', 'egg beater', 'egg timer', 'espresso machine', 'food processor', 
'garlic press', 'hamburger press', 'hand mixer', 'ice bucket', 'ice cream scoop', 
'icing spatula', 'jar opener', 'measuring cup', 'mixing bowl', 'mortar and pestle', 
'nut cracker', 'parchment paper', 'pastry bag', 'pepper mill', 'pizza cutter', 
'pizza stone', 'popcorn popper', 'pressure cooker', 'raclette grill', 'rice cooker', 
'rolling pin', 'salad bowl', 'salad spinner', 'salt shaker', 'sharpening steel', 
'slow cooker', 'souffle dish', 'spice rack', 'vegetable bin', 'waffle iron', 
'water filter', 'yogurt maker']

descriptors = ['Fresh', 'Natural', 'Pure', 'Traditional', 'Original', 'Authentic', 'Real', 'Genuine',
'Home(.*)made', 'Farmhouse', 'Hand(.*)made', 'Premium', 'Finest', 'Quality', 'Best', 'crushed', 'all-purpose',
               'Montreal', 'cube','packet','dry', 'dried', 'freshly', 'ground', 'packed','chopped', 'Italian',
               'jar','whole milk', 'skim', 'whole','half','crushed','shredded', 'frozen', 'thawed'] # may need to remove 'whole milk' in case there is an ingredient 'whole milk'

preparation = ['bake', 'barbecue', 'baste', 'beat', 'bind', 'blanch', 'blend', 'boil', 
'bone', 'braise', 'bread', 'broil', 'brown', 'brush', 'candy', 'caramelize', 'chill', 
'chop', 'clarify', 'coat', 'coddle', 'combine', 'cool', 'core', 'cream', 'crush', 
'cube', 'cut', 'cut in', 'deep-fry', 'devein', 'dice', 'dissolve', 'dot', 'drain', 
'dredge', 'dress', 'dust', 'elevate', 'flake', 'flour', 'flute', 'fold', 'fricassee', 
'fry', 'garnish', 'glaze', 'grate', 'grease', 'grill', 'grind', 'hull', 'julienne', 
'knead', 'marinate', 'mash', 'melt', 'mince', 'mix', 'mold', 'panboil', 'panfry', 
'parboil', 'pare', 'peel', 'pit', 'poach', 'preheat', 'punch down', 'puree', 'quarter', 
'reconstitute', 'reduce', 'refresh', 'roast', 'roll', 'rotate', 'saute', 'scald', 
'scallop', 'score', 'sear', 'season', 'section', 'shape', 'shell', 'shield', 'shred', 
'sift', 'simmer', 'skim', 'slice', 'sliver', 'snip', 'sprinkle', 'steam', 'steep', 
'sterilize', 'stew', 'stir', 'stir-fry', 'strain', 'thicken', 'toast', 'toss', 'truss', 
'unmold', 'vent', 'whip','whisk']

# Each sentense is a step.

# Step:
# dic = {1: {'ingredient':[
#                         {'Name': ...,
#                          'Quantity': ..., 
#                          'Measurement': ...,
#                          'Descriptor': ...,
#                          'Preparation': ...,
#                          },
#                          {'Name': ...,
#                          'Quantity': ..., 
#                          'Measurement': ...,
#                          'Descriptor': ...,
#                          'Preparation': ...,
#                          },
#                          ...
#                          ]
#             'tool': ...,
#             'method': ...,
#             'time': ...,
#             },
#         2: {},
#     }


# 1. Descriptor, Preparation, Time
# 2. Step
# 3. Transform


"""takes in allrecipes.com recipe url, returns parsed HTML"""
def process_html(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup

"""takes in prettified recipe url, returns either list of ingredients or directions"""
def scrape_x(url, component): #either ingredient or direction
    soup = url
    if component == 'ingredient':
        items = soup.find_all("span", itemprop="ingredients")
    elif component == 'direction':
        items = soup.find_all("span", class_='recipe-directions__list--item')
    else:
        return -1
    item_lst = []
    for elt in items:
        if elt.string:
            item_lst.append(elt.string.encode('ascii')) #.encode('ascii')
    return item_lst

def parse_ingredient(ln):
    """
    :param ln: an ingredient in format quantity, measurement, ingredient name, descriptor
    :rtype : 4 strings: item_name, quantity, measurement, descriptor
    """
    # if ln.endswith("to taste"):
    #     # need o add descriptor handling
    #     quantity = "to taste"
    #     measurement = ''
    #     descriptor =''
    #     item  = ln[:-9]
    #
    #     return item, quantity, measurement, descriptor
    lst = ln.split(' ')
    quantity = lst[0]
    measurement = []
    i = 1
    if '/' in lst[i]:
        quantity += ' {0}'.format(lst[1])
        i = 2
    if '(' in lst[i]: # case where measurement has parens (e.g. '(19 oz can of beans)')
        k = i
        end = False
        while end != True: #')' not in lst[i]:
            if ')' in lst[k]:
                end = True
            measurement.append(lst[k])
            k += 1
        measurement = ' '.join(measurement).translate(None,string.punctuation) #strips parens off string
        i = k
    elif lst[i] in measurements:
        measurement = lst[i]
        i += 1
    else:
        measurement = ''
        i = 1
    item_desc = ' '.join(lst[i:]).split(',')
    if len(item_desc) > 1:
        item = item_desc[0]
        descriptor = item_desc[1].lstrip()
    else:
        item = item_desc[0]
        descriptor = ''

    # handle descriptors
    for d in descriptors:
        if d in item and d not in descriptor:
            descriptor += ' {0}'.format(d)
            item = item.replace(d,'')
            item = item.strip(' ')
    descriptor = descriptor.strip(' ')
    return item, quantity, measurement, descriptor

def ingredients_to_dict(ing_list):
    # need to include cooking methods/ cooking tools pulled directions.... TB done later
    # takes list of ingredients as input, returns dictionary of ingredients, cooking method, cooking tools formatted as such:
    # format dict: {"ingredients": [{
    #                                   "name": str,
    #                                   "quantity":int,
    #                                   "measurement": str,
    #                                   "descriptor":str,
    #                                   "preparation":str}
                                #   {   "name": str, "quantity":...
    #                             ...]
    #                "cooking method": "str"
    #                "cooking tools": ["str", "str",...] }
    recipe_dict = {"ingredients":[], "cooking method":'', "cooking tools":[]}
    for ingredient in ing_list:
        i_dict = {"name": '', "quantity":'', "measurement": '', "descriptor":'', "preparation":''}
        vals = parse_ingredient(ingredient) # item, quantity, measurement, descriptor
        # print vals
        i_dict["name"] = vals[0]
        i_dict["quantity"] = vals[1]
        i_dict["measurement"] = vals[2]
        i_dict["descriptor"] = vals[3]
        recipe_dict["ingredients"].append(i_dict)
    return recipe_dict

def ingredients_to_lists(ing_list):
    names = []
    quantities = []
    measurements =[]
    descriptors = []
    for ing in ing_list:
        vals= parse_ingredient(ing) # (n,m,q,d)
        names.append(vals[0])
        quantities.append(vals[1])
        measurements.append(vals[2])
        descriptors.append(vals[3])

    return names,quantities,measurements, descriptors

def print_directions(lst):
    directions = lst
    count = 1
    for i in directions:
        print "{0}) {1}".format(count,i)
        count += 1
    return 0

# splits direcitons by sentences + flattens list/ removes leading spaces
def parse_directions(dir_list):
    d_list = []
    for i in range(len(dir_list)):
        d_list.append(dir_list[i].split('.'))
    return [item.lstrip() for sublist in d_list for item in sublist if item]
#   return format: dict = {'tools':[str],'methods':[str], 'ingredients':[{n,q,m,d,p}...], 'steps': [{'method':'', 'ingredients':[str],'tools':[str], 'text':''}
# parsed_vals = {
# 	"tools": ["", ""],
# 	"methods": ["", ""],
# 	"ingredients": [
# 	    {
# 			"preparation": "",
# 			"descriptor": "",
# 			"measurement": "",
# 			"name": "clove garlic",
# 			"quantity": "1"
# 	    },
# 	    {'name':""...}],
# 	"steps": [
# 		{
# 			"method": "",
# 			"ingredients": ['garlic', 'chicken'],
# 			"tools": ["knife","spoon"],
# 			"text": ""
# 		},
# 		{...}]
# }

# iterate through steps in direction list, for each step, get the ingredient(s) involved, tools/ methods and put in dict
# builds new direction dict by getting relevant ingredient info by index in each respective list
def steps_to_dict(d_list,i_lst):
    # issues: searching for compound-word ingredients in directions (not typically referenced by exact name)
    #       can be solved in initial parsing... maybe search for combinations of bigrams?
    names, quants, measurements, descriptors = ingredients_to_lists(i_lst)
    drxn_dict = {'tools':[], 'methods':[],'ingredients':[], 'steps':[]}
    # create ingredients list of dicts
    for i in names:
        if i not in drxn_dict['ingredients']:
            new_ing = {'name':'', 'quantity':'','measurement':'','descriptor':'', 'preparation':''}
            ing_index = names.index(i)
            new_ing['name'] = i
            new_ing['quantity'] = quants[ing_index]
            new_ing['measurement'] = measurements[ing_index]
            new_ing['descriptor'] = descriptors[ing_index]
            drxn_dict['ingredients'].append(new_ing)
    # create populate tools, methods, steps
    for dir in d_list:
        dir_cleaned = dir.translate(None, string.punctuation)
        ingreds = cu.find_term(dir_cleaned, names)
        tools = cu.find_term(dir_cleaned, cooking_tools_one) + cu.find_term(dir_cleaned, cooking_tools_two)
        methods = cu.find_term(dir_cleaned, cooking_methods)

        for t in tools:
            if t not in drxn_dict['tools']:
                drxn_dict['tools'].append(t)
        for m in methods:
            if m not in drxn_dict['methods']:
                drxn_dict['methods'].append(m)
        # add to steps
        step = {'method':[], 'ingredients':[],'tools':[], 'text':''}
        step['method'] = methods
        step['ingredients'] = ingreds
        step['tools'] = tools
        step['text'] = dir
        drxn_dict['steps'].append(step)
        # in a single step:
        # get ingredients+ relevant info (name, quant,descriptor*, prep*)
        # get tools involved
        # get cooking method used

    return drxn_dict

def main(url):
    page = process_html(url)
    ingredients = scrape_x(page, 'ingredient') # ingredients =  scrape_x(page, 'ingredient')
    # ingredients_dict = ingredients_to_dict(ingredients)
    # names,quants,measurements, descriptors = ingredients_to_lists(ingredients)
    directions = parse_directions(scrape_x(page, 'direction'))  # directions =  scrape_x(page, 'direction')
    steps_dict = steps_to_dict(directions, ingredients)


    # print ingredients
    return json.dumps(steps_dict, indent=2)
    # return json.dumps(ingredients_dict, indent=2) #json.dumps returns pretty format dict

print main(recipe_url)