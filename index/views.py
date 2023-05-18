from django.http import JsonResponse

from .models import WordIndex
from index.helpers.lemmatize_request import lemmatize

def index(request):
    return HttpResponse("Hello! You can look up a word using GET /index/your-word")

def get_word(request, word):
	lemmatized_request = lemmatize(word.lower())
	resp = WordIndex.objects.filter(word=lemmatized_request)
	if not resp:
		return JsonResponse(None, safe=False) # return None per instructions
	return JsonResponse(resp[0].index_data)