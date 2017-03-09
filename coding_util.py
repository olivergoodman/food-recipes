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