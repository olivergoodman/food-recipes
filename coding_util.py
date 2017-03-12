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

# 'abc. 123.' -> ['abc','123']
def split_sentences(text):
    '''
	split text into list of sentences
	'''
    sentences = re.split(r' *[\.\?!\n*][\'"\)\]]* *',text)
    return filter(lambda x: len(x)>0,sentences)


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