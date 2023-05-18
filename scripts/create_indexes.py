import json
import sys
import spacy
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex

STORY_PATH = sys.argv[1]
# container needed in the format to load into django
JSON_OUT = []
# keep track of words and primary keys
WORDS_SEEN = []

# load the tokenizer and lemmatizer
# amend the tokenization rule that splits on hyphens
# code here taken from the spacy documentation
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

# creates or updates the json blob to load into django
def append_lemma(token, line_number):
	lemma = token.lemma_

	# if we've seen the word already update its information
	existing_entry_blob = next((item for item in JSON_OUT if item["fields"]["word"] == lemma), None)
	if existing_entry_blob:
		existing_entry_blob["fields"]["index_data"]["count"] += 1
		if line_number not in existing_entry_blob["fields"]["index_data"]["lines"]:
			existing_entry_blob["fields"]["index_data"]["lines"].append(line_number)
		pk_index = existing_entry_blob["pk"] - 1
		JSON_OUT[pk_index] = existing_entry_blob

	# otherwise create a new entry
	else:
		new_pk = len(WORDS_SEEN) + 1
		new_entry_blob = {
			"model": "selectstar.wordindex",
			"pk": new_pk,
			"fields": {
				"word": lemma,
				"index_data": {
					"count": 1,
					"lines": [line_number]
				}
			}
		}
		JSON_OUT.append(new_entry_blob)
		WORDS_SEEN.append(lemma)

def create_dictionary():
	with open(STORY_PATH) as story:
		for line_number, line in enumerate(story):
			#lowercase and tokenize the line
			tokens = nlp(line.lower())

			for token in tokens:
				# ignore non-words
				if token.pos_ not in ['PUNCT', 'SPACE']:
					append_lemma(token, line_number)
					# if hyphenated we process the entire token and each part
					if '-' in token.text:
						new_tokens = nlp(' '.join(token.text.split('-')))
						for token in new_tokens:
							append_lemma(token, line_number)

						
						
create_dictionary()
# TODO: need to lemmatize hyphenated words properly: we save 'shape-shifting' ❓, 'shape' ✅ , and 'shift' ✅  but it might need to be 'shape-shift'
with open("../fixtures/word_index.json", "w") as outfile:
	json.dump(JSON_OUT, outfile)
