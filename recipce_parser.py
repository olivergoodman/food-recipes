__author__ = 'cmark'
from bs4 import BeautifulSoup
import urllib2
import json
import re

# test urls
recipe_url = 'http://allrecipes.com/recipe/235710/chef-johns-ricotta-meatballs/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=235710&referringContentType=recipe'
rec = 'http://allrecipes.com/recipe/191793/country-fried-steak/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%201'

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
 'STERILIZE', 'STEW', 'STIR', 'TOSS', 'TRUSS', 'WHIP']

# simple cooking tool terms
cooking_tools_one = ['apron', 'baster', 'blender', 'carafe', 'colander', 'cookbook', 
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
'Home(.*)made', 'Farmhouse', 'Hand(.*)made', 'Premium', 'Finest', 'Quality', 'Best']

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
'unmold', 'vent', 'whip']

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

def scrape_ingredients(url):
    # page = urllib2.urlopen(url)
    # soup = BeautifulSoup(page, "html.parser")
    soup = url
    ingredients = soup.find_all("span", itemprop="ingredients")
    ing_list = []
    for elt in ingredients:
        ing_list.append(elt.string) # .encode('ascii')
    return ing_list

def scrape_directions(url):
    soup = url
    directions = soup.find_all("span", class_='recipe-directions__list--item')
    direction_list = []
    for drxn in directions:
        direction_list.append(drxn.string) #.encode('ascii')
    return direction_list
# print scrape_ingredients(recipe_url)

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

# # parses a single line of ingredient... format: quantity measurement item
# def parse_ingredient1(ln):
#     lst = ln.split(' ')
#     quantity = lst[0]
#     measurement = []
#     if '(' in lst[1]: # case where measurement has parens (e.g. '(19 oz can of beans)')
#         i = 1
#         end = False
#         while end != True: #')' not in lst[i]:
#             if ')' in lst[i]:
#                 end = True
#             measurement.append(lst[i])
#             i += 1
#         measurement = ' '.join(measurement).translate(None,"()") #strips parens off string
#     elif '/' in lst[1]:
#         quantity += ' {0}'.format(lst[1])
#         i = 2
#     elif lst[1] in measurements:
#         measurement = lst[1]
#         i = 2
#     else:
#         measurement = ''
#         i = 1
#     item = ' '.join(lst[i:])
#     return quantity, measurement, item

def parse_ingredient(ln):
    if ln.endswith("to taste"):

        quantity = "to taste"
        measurement = []
        item  = ln[:-9]

        return quantity, measurement, item
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
        measurement = ' '.join(measurement).translate(None,"()") #strips parens off string
        i = k
    elif lst[i] in measurements:
        measurement = lst[i]
        i += 1
    else:
        measurement = ''
        i = 1
    item = ' '.join(lst[i:])
    return quantity, measurement, item

def format_ingredients(ing_list):
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
        q,m,i = parse_ingredient(ingredient) #quantity, measurement, item
        i_dict["name"] = i
        i_dict["quantity"] = q
        i_dict["measurement"] = m
        recipe_dict["ingredients"].append(i_dict)

    return recipe_dict


def main(url):
    page = process_html(url)
    ingredients = scrape_x(page, 'ingredient') # ingredients =  scrape_x(page, 'ingredient')
    ingredients_dict = format_ingredients(ingredients)
    # directions = scrape_x(page, 'direction')  # directions =  scrape_x(page, 'direction')

    return json.dumps(ingredients_dict, indent=2) #json.dumps returns pretty format dict
    # return directions

print main(recipe_url)

# print parse_ingredient1('1 1/2 (28 ounce) jar marinara sauce')
# print parse_ingredient1('1 cup chopped onion')