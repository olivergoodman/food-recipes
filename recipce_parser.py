__author__ = 'cmark'
from bs4 import BeautifulSoup
import urllib2
import json

# test urls
recipe_url = 'http://allrecipes.com/recipe/235710/chef-johns-ricotta-meatballs/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=235710&referringContentType=recipe'
rec = 'http://allrecipes.com/recipe/191793/country-fried-steak/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%201'

# probably a better way to do this and be able to exclude plurals
measurements = ['cup', 'cups', 'teaspoon', 'teaspoons', 'tablespoon','tablespoons','quart','quarts','gallon', 'gallons',
                'litre','litres', 'pint', 'pints', 'pinch', 'pinches', 'pound', 'pounds', 'ounce', 'ounces' 'fluid ounce', 'fluid ounces']

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

# parses a single line of ingredient... format: quantity measurement item
def parse_ingredient(ln):
    lst = ln.split(' ')
    print lst
    # need to handle measurements like '1 1/2' teaspoons...
    # if 'to taste' in ln:
    #     quantity = ['to taste']
    #     name = lst

    quantity = lst[0]
    measurement = []
    if '(' in lst[1]: # case where measurement has parens (e.g. '(19 oz can of beans)')
        i = 1
        end = False
        while end != True: #')' not in lst[i]:
            if ')' in lst[i]:
                end = True
            measurement.append(lst[i])
            i += 1
        measurement = ' '.join(measurement).translate(None,"()") #strips parens off string
    elif '/' in lst[1]:
        quantity += ' {0}'.format(lst[1])
        i = 2
    elif lst[1] in measurements:
        measurement = lst[1]
        i = 2
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

def print_directions(lst):
    directions = lst
    count = 1
    for i in directions:
        print "{0}) {1}\n".format(count,i)
        count += 1
    return 0

def main(url):
    page = process_html(url)
    ingredients = scrape_x(page, 'ingredient') # ingredients =  scrape_x(page, 'ingredient')
    ingredients_dict = format_ingredients(ingredients)
    directions = scrape_x(page, 'direction')  # directions =  scrape_x(page, 'direction')

    return json.dumps(ingredients_dict, indent=2) #json.dumps returns pretty format dict
    # return print_directions(directions)

print main(rec)

# print parse_ingredient('1 (28 ounce) jar marinara sauce')
# print parse_ingredient('1 cup chopped onion')