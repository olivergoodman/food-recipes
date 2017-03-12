import re
import string
def find_term(sentence, term_list):
    '''
	find which term in term_list exists in the sentence
	'''
    terms =[]
    for term in term_list:
        m = re.search(term, sentence, re.IGNORECASE)
        if m:
            terms.append(term)
    return terms

def find_term_by_direction(sentence, ingred_list):
    '''
    takes in a sentence cleaned of punctuation, list of ingredients
    search for each word in a direction for its existence in ingred_list
    returns ingredient name
    '''
    terms = []
    direc_lst = sentence.split(' ')
    for d in direc_lst:
        if d not in stopwords:
            for i in ingred_list:
                if d in i and i not in terms:
                    terms.append(i)
    return terms

# 'abc. 123.' -> ['abc','123']
def split_sentences(text):
    '''
	split text into list of sentences
	'''
    sentences = re.split(r' *[\.\?!\n*][\'"\)\]]* *',text)
    return filter(lambda x: len(x)>0,sentences)

def print_help(s):
    if s != '':
        print s,

def print_list(l):
    for x in l:
        print '%s;'%x,
    print

def print_recipe_readable(recipe):
    ingredient_list = recipe['ingredients']
    tool_list = recipe['tools']
    method_list = recipe['methods']
    step_list = recipe['steps']

    print "The ingredients you need:"
    for ingred in ingredient_list:
        print "\t",
        print_help(ingred['quantity'])
        print_help(ingred['measurement'])
        print_help(ingred['descriptor'])
        print_help(ingred['preparation'])
        print_help(ingred['name'])
        print
    print

    print "The tools you need:"
    for tool in tool_list:
        print '\t%s'%tool
    print

    print "Methods:"
    for me in method_list:
        print '\t%s'%me.lower()
    print

    print "Directions:"
    i = 1
    for step in step_list:
        print "Step %d:"%i
        print "\tingredients:",
        print_list(step['ingredients'])
        print "\ttools:",
        print_list(step['tools'])
        print "\tmethods:",
        print_list(step['method'])
        print "\tdirection: %s\n"%step['text']
        i += 1

primary_cooking_methods = ['BAKE', 'BOIL', 'BROIL', 'FRY', 'GRILL', 'PAN-BROIL', 
'PAN-FRY', 'PARBOIL', 'POACH', 'ROAST', 'SAUTE', 'SIMMER', 'STEAM', 'STEW', 'STIR']

other_cooking_methods = ['AL DENTE', 'BARBECUE', 'BASTE', 'BATTER', 'BEAT', 'BLANCH', 
'BLEND', 'CARAMELIZE', 'CHOP', 'CLARIFY', 'CREAM', 'CURE', 'DEGLAZE',
 'DEGREASE', 'DICE', 'DISSOLVE', 'DREDGE', 'DRIZZLE', 'DUST', 'FILLET', 'FLAKE', 
 'FLAMBE', 'FOLD', 'FRICASSEE', 'GARNISH', 'GLAZE', 'GRATE', 'GRATIN', 
 'GRIND', 'JULIENNE', 'KNEAD', 'LUKEWARM', 'MARINATE', 'MEUNIERE', 'MINCE', 'MIX', 
 'PARE', 'PEEL', 'PICKLE', 'PINCH', 'PIT', 'PLANKED', 
 'PLUMP', 'PUREE', 'REDUCE', 'REFRESH', 'RENDER', 'SCALD', 
 'SCALLOP', 'SCORE', 'SEAR', 'SHRED', 'SIFT', 'SKIM', 'STEEP', 
 'STERILIZE', 'TOSS', 'TRUSS', 'WHIP', 'WHISK']

stopwords = ['and', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
             'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
             'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
             'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
             'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
             'did', 'doing', 'a', 'an', 'the', 'but', 'if', 'or', 'because', 'as', 'until',
             'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
             'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
             'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
             'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
             'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
             'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']