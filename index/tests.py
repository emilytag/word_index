from django.test import TestCase
from .models import WordIndex
from index.helpers.lemmatize_request import lemmatize
from django.urls import reverse

class WordIndexModelTests(TestCase):
	# cant use these on the unit testing level because it needs to access the built db
	'''
	# check some words we expect to be present in the db
	def test_word_index(self):
		# try an easy one
		word1 = WordIndex.objects.filter(word="once")[0].index_data
		self.assertEqual(word1, {"count": 2, "lines": [1, 94]})

		# try a word that we know should be lemmatized
		word2 = WordIndex.objects.filter(word="hope")[0].index_data
		self.assertEqual(word2, {"count": 2, "lines": [14, 96]})

		# try a unicode word
		word3 = WordIndex.objects.filter(word="🗝")[0].index_data
		self.assertEqual(word3, {"count": 3, "lines": [71, 76, 104]})

		# try a hyphenated word
		word4 = WordIndex.objects.filter(word="héctor-andrés")[0].index_data
		self.assertEqual(word4, {"count": 12, "lines": [0, 2, 3, 5, 9, 14, 19, 23, 27, 29, 33, 35]})
		'''

	#  check a word we don"t expect to be present in the db
	def test_no_index(self):
		word = list(WordIndex.objects.filter(word="westwood"))
		self.assertEqual(word, [])


	# todo: set up some integration-level tests for the views
	# on hold while i read the docs about that in django
	def test_get_word_response(self):
		url = reverse('get_word', args=['sky'])
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		# self.assertEqual('placeholder', resp.content) # on hold until i can populate db for tests


class LemmatizerTests(TestCase):
	# check that the lemmatizer works as expected
	def test_word_lemmas(self):
		lemma1 = lemmatize("hoping")
		self.assertEqual(lemma1, "hope")

		lemma2 = lemmatize("hunting")
		self.assertEqual(lemma2, "hunt")

	# we do not expect the application lemmatizer to split on hyphens
	def test_hyphenated_words(self):
		lemma1 = lemmatize("héctor-andrés")
		self.assertEqual(lemma1, "héctor-andrés")

		lemma2 = lemmatize("金-ὐνιϲσδε-dwellers")
		self.assertEqual(lemma2, "金-ὐνιϲσδε-dweller")