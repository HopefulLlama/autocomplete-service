from django.shortcuts import render
from django.http import JsonResponse
from autocomplete.suggester import Suggester

suggester = Suggester("hello/autocomplete/words.txt")

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def autocomplete(request):
    prefix = request.GET.get('prefix', '')
    if len(prefix) is 0:
        return JsonResponse([], safe=False)
    else:
        suggestions = suggester.get_suggestions(prefix)
        return JsonResponse(suggestions, safe=False)
