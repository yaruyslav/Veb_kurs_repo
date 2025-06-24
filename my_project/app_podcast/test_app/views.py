from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

class User:
    id = 0

class Admin:
    id = 0

class Item_group:
    id = 0

class Sorter:
    id = 0

class Rec_service:
    id = 0

class Search_service:
    id = 0

class Get_user:
    id = 0

class Get_author:
    id = 0

class Get_podcast:
    id = 0

class Get_episode:
    id = 0

class Get_rating:
    id = 0



def login(request):
    return render(request, 'entrace_enter.html')

def register(request):
    return render(request, 'entrace_register.html')

stringg = "lalallananananna"
def general_page(request):
    context = {
        'str': stringg,
    }
    return render(request, 'base_general.html', context)

def test_app():
    template = loader.get_template('index.html')
    return HttpResponse(template.render())