from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def snippets_list(request):
    name =[ 'bob', 'jackson', 'leo', 'maz']
    return render(request, 'snippets/snippets_list.html', {'name_key':name})

def snippets_details(request, id):
    return HttpResponse(f'snippets_favourite with id of {id}')
