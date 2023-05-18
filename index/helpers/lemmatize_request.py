import spacy
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex


nlp = None
# this and get_lemmatizer will load the spacy model if not already loaded in that session
def load_spacy():
	global nlp

	nlp = spacy.load("en_core_web_sm")
	infixes = (
    	LIST_ELLIPSES
    	+ LIST_ICONS
    	+ [
    	    r"(?<=[0-9])[+\\-\\*^](?=[0-9-])",
     	   r"(?<=[{al}{q}])\\.(?=[{au}{q}])".format(
    	        al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
    	    ),
    	    r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
   	    	# ✅ Commented out regex that splits on hyphens between letters:
   	    	# r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
        	r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
    	]
	)
	infix_re = compile_infix_regex(infixes)
	nlp.tokenizer.infix_finditer = infix_re.finditer

def get_lemmatizer():
	if nlp is None:
		load_spacy()
	return nlp

# TODO: multi-word requests?
def lemmatize(word):
	nlp = get_lemmatizer()
	first_token = nlp(word)[0]
	return first_token.lemma_