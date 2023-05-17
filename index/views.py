from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! You can look up a word using GET index/your-word")

def get_word(request, word):
	# TODO
	#word_found = get_word(word)
	word_indexes = 'ok!!'
	return HttpResponse(word_indexes)