from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import User
from .classes.services import *
from .classes.table_interfaces import *
from .classes.storage_classes import *
from django.conf import settings
import random



def login(request):
    if 'logining' in request.session and request.session['logining']==1:
        request.session['logining'] = 0
        return redirect('GENERAL')
    
    context = {
        'error': '',
        'is_show': False,
    }
    if 'is_show' not in request.session:
        request.session['is_show'] = False
    if 'error' in request.session:
        context['error'] = request.session['error']
        context['is_show'] = True
    
    if (request.method=="POST"):
        name = request.POST.get("login")
        passw = request.POST.get("passw")
        usr = None
        for i in User.objects.all().values():
            if (i['name']==name):
                if (i['password']==passw):
                    usr = i
                    break
        if (usr):
            request.session.clear()
            request.session['usr_id'] = usr['id']
            request.session['usr_name'] = usr['name']
            request.session['usr_rights'] = usr['rights']
            request.session['logining'] = 0
            if (usr['rights']==1 or usr['rights']==2):
                return redirect('GENERAL')
            else:
                context['error'] = "Помилка при отриманні даних користувача!"
        else:
            context['error'] = "Ви не правильно ввели логін чи пароль!"
        if (context['error']):
            context['is_show'] = True
        else:
            context['is_show'] = False

    request.session['is_show'] = context['is_show']
    return render(request, 'main/entrace/entrace_enter.html', context)


def register(request):
    request.session.clear()
    context = {
        'error': '',
        'is_show': False,
    }
    if 'is_show' not in request.session:
        request.session['is_show'] = False
    if 'error' in request.session:
        context['error'] = request.session['error']
        context['is_show'] = True

    if (request.method=="POST"):
        name = request.POST.get("login")
        passw = request.POST.get("passw")
        rpassw = request.POST.get("repassw")
        
        if (name and passw and rpassw):
            is_duble = False
            for obj in User.objects.all().values():
                if obj['name']==name:
                    is_duble = True
                    break
            if (not is_duble):
                if (passw==rpassw):
                    user_create_st = Set_user().create(name, passw, 2, "1234-12-13")
                    if (user_create_st!=False):
                        user = Get_user().get_user_by_id(user_create_st)
                        if (user!=False):
                            request.session.clear()
                            request.session['usr_id'] = user['id']
                            request.session['usr_name'] = user['name']
                            request.session['usr_rights'] = user['rights']
                            request.session['logining'] = 1
                            return redirect("LOGIN")
                        else:
                            context['error'] = "Дані користувача не знайдено або вони введені не вірно!"
                    else:
                        context['error'] = "Дані введені не вірно!"
                else:
                    context['error'] = "Паролі не повторюються!"
            else:
                context['error'] = "Користувач під іменем '" + name + "' вже існує!"
        else:
            context['error'] = "Ви не ввели дані!"
        if (context['error']):
            context['is_show'] = True
        else:
            context['is_show'] = False

    request.session['is_show'] = context['is_show']
    return render(request, 'main/entrace/entrace_register.html', context)


def entre_page(request):
    return redirect("LOGIN")
    # return render(request, 'main/users/admin_pages/pg_general.html')



def general_page(request):
    if 'error' in request.session:
        request.session.pop('error')

    if (request.method=="POST"):
        type = request.POST.get('exit')
        if type=='1':
            request.session.clear()
            return redirect("LOGIN")

    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'usr_id': request.session['usr_id'],
        'usr_name': request.session['usr_name'],
        'usr_rights': request.session['usr_rights'],
        'logining': request.session['logining'],
        'set_elem': [],
        
        'test_value': 'No method! :(',
        'test_tuser': '',
    }


    def regular_render():
        context['test_tuser'] = 'user'
        return render(request, 'main/users/regular_pages/pg_general.html', context)
    

    def admin_render():
        context['test_tuser'] = 'admin'

        # set_data = Rec_service().get_rand_episodes()
        # elements = []                                          # типу цього ['тема', [обж1, обж2]]
        # aviable_elem = set_data.copy()
        # for i in range(len(aviable_elem)):
        #     ind = random.randint(0, len(aviable_elem)-1)
        #     el = aviable_elem.pop(ind)
        #     elements.append(el)
        #     if i==4:
        #         break
        # context['set_elem'].append(['', elements])

        set_data = Rec_service().get_rand_episodes(5)
        elements = []                                          # типу цього ['тема', [обж1, обж2]]
        for el in set_data:
            elements.append(el)
        context['set_elem'].append(['', elements])

        # array = ['title1', []]
        # for i in range(0,5):
        #     elem = El_author(type=El_author.__name__, id=i, title="auuuuuuuthooooorrrr"+str(i+1))
        #     array[1].append(elem)
        # context['set_elem'].append(array)

        # array = ['title2', []]
        # for i in range(0,5):
        #     elem = El_other(type=El_other.__name__, id=i, title="othreeeerrrer"+str(i+1))
        #     array[1].append(elem)
        # context['set_elem'].append(array)

        # array = ['title3', []]
        # for i in range(0,5):
        #     elem = El_episode(type=El_episode.__name__, id=i, title="epipipisodedede"+str(i+1), descr="descr"+str(i+1), add="addition"+str(i+1))
        #     array[1].append(elem)
        # context['set_elem'].append(array)

        # array = ['title4', []]
        # for i in range(0,5):
        #     elem = El_podcast(type=El_podcast.__name__, id=i, title="podpodpodcastasssst"+str(i+1))
        #     array[1].append(elem)
        # context['set_elem'].append(array)

        # array = ['title5', []]
        # for i in range(0,5):
        #     elem = El_playlist(type=El_playlist.__name__, id=i, title="playplayplayfromlistlist"+str(i+1))
        #     array[1].append(elem)
        # context['set_elem'].append(array)

        if (request.method == 'POST'):
            context['test_value'] = 'This is POST! ;)'

        return render(request, 'main/users/admin_pages/pg_general.html', context)


    # if 'usr_id' in request.session:
    if (request.session['usr_rights']==1):
        return regular_render()
    elif (request.session['usr_rights']==2):
        return admin_render()

    request.session['error'] = 'Помилка при пошуку сторінки!'
    return redirect("BASE")




def search_page(request):
    type = request.GET.get('type')
    if (request.method=="POST"):
        type = request.POST.get('exit')
        if type=='1':
            request.session.clear()
            return redirect("LOGIN")
    elif (type):
        if type=='get_link':
            id = request.GET.get("id")
            if not Get_episode().get_more_by_id(id):
                return JsonResponse({'MEDIA_NAME': None})
            link = Get_episode().get_more_by_id(id)[0]
            if link:
                return JsonResponse({'MEDIA_NAME': link})
        return JsonResponse({'MEDIA_NAME': None})
    
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'usr_id': request.session['usr_id'],
        'usr_name': request.session['usr_name'],
        'usr_rights': request.session['usr_rights'],
        'logining': request.session['logining'],
        'set_elem': [],
    }


    def regular_render():
        return render(request, 'main/users/regular_pages/pg_search.html', context)
    

    def admin_render():
        set_data = Rec_service().get_all_episodes()
        elements = []                                                # ['', []]
        for el in set_data:
            elements.append(el)
        context['set_elem'].append(['Всі епізоди', elements])

        return render(request, 'main/users/admin_pages/pg_search.html', context)


    if (request.session['usr_rights']==1):
        return regular_render()
    elif (request.session['usr_rights']==2):
        return admin_render()

    request.session['error'] = 'Помилка при пошуку сторінки!'
    return redirect("BASE")



def outset_page(request):
    if 'error' in request.session:
        request.session.pop('error')
        
    context = {
        'id_plist': '',                                     # просто для наглядності
        'MEDIA_URL': settings.MEDIA_URL,
        'usr_id': request.session['usr_id'],
        'usr_name': request.session['usr_name'],
        'usr_rights': request.session['usr_rights'],
        'logining': request.session['logining'],
        'set_elem': [],
    }

    type = request.GET.get('type')
    if (request.method=="POST"):
        type = request.POST.get('exit')
        if type=='1':
            request.session.clear()
            return redirect("LOGIN")
    elif (type):
        if (type=='get_listdata'):
            id = request.GET.get('id')
            context['id_plist'] = id

            # set_data = Rec_service().get_all_episodes()                     # тутаааааа!!!"!!"!"!"!""
            # elements = []
            # aviable_elem = set_data.copy()
            # for i in range(len(aviable_elem)):
            #     ind = random.randint(0, len(aviable_elem)-1)
            #     el = aviable_elem.pop(ind)
            #     elements.append(el)
            #     if i==1:
            #         break
            play_lists = Get_user().getSetDataById(context['usr_id'])
            plist_name = ''
            for el in play_lists:
                if el.id==context['id_plist']:
                    play_lists = el['name']
            data_plist = Get_playlist().get_setdata_by_id(context['id_plist'])
            elements = []
            for el in data_plist:
                elements.append(el)
            context['set_elem'].append([plist_name, elements])
            return render(request, 'main/users/content_output.html', context)


    def regular_render():
        return render(request, 'main/users/regular_pages/pg_set.html', context)


    def admin_render():
        if request.method=="POST":
            pass

        set_data = Get_user().getSetDataById(context['usr_id'])
        elements = []
        for el in set_data:
            elem = El_playlist(type=El_playlist.__name__, id=el.id, title=el.name, add='')                              #"id_user: "+str(el.id_user)
            elements.append(elem)
        context['set_elem'].append(['Списки відтворення', elements])

        return render(request, 'main/users/admin_pages/pg_set.html', context)
    

    if (request.session['usr_rights']==1):
        return regular_render()
    elif (request.session['usr_rights']==2):
        return admin_render()

    return render(request, 'main/users/admin_pages/pg_set.html', context)




def test_app():
    template = loader.get_template('index.html')
    return HttpResponse(template.render())







# stringg = "lalallananananna"
# def general_page(request):
#     num = 0
#     out = ''
#     object = Podcast.objects.all().values()
#     if object:
#         for line in object:
#             if line['name']=='Alex':
#                 break
#             else:
#                 out = "Fail!((("
#                 break
#             num = num + 1
#     else:
#         out = "Fail!((("
#     if not out:
#         out = object[num]

#     context = {
#         'str': stringg,
#         'id': out,
#     }
#     return render(request, 'base_general.html', context)