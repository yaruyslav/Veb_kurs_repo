import sys
import os

from main.models import *
from main.models import User
from .storage_classes import *


class Get_user:
    def get_user_by_id(self, id):
        storage = User.objects.all().values()
        for el in storage:
            if el['id']==id:
                return el
        return False
    
    def getDataByName(self, get_name):
        id = -1
        name = ''
        password = ''
        rights = -1
        storage = User.objects.all().values()
        for el in storage:
            if el['name']==get_name:
                id = el['id']
                name = el['name']
                password = el['password']
                rights = el['rights']
                break
        if rights==1:
            return User_data(id=id, name=name, passw=password, rights=rights)
        elif rights==2:
            return Admin_data(id=id, name=name, passw=password, rights=rights)
        return None

    def getSetDataById(self, get_id):
        data_set = []
        storage = User.objects.all().values()
        for el in storage:
            if el['id']==get_id:
                set_storage = User_groups.objects.all().values()
                for g_el in set_storage:
                    if g_el['id_user_id']==el['id']:
                        g_id = g_el['id']
                        g_name = g_el['name']
                        g_id_user = g_el['id_user_id']
                        data_set.append(Usr_group(g_id, g_name, g_id_user))
                break
        return data_set


class Get_episode:
    def get_Episodes_By_Command(self, comm):
        data_set = []
        if (comm=="all"):
            storage = Episode.objects.all().values()
            for el in storage:
                id = el['id']
                name = el['name']
                id_podcast = el['id_podcast_id']
                duration = ''
                data_set.append(El_episode(type=El_episode.__name__, id=id, title=name, descr='', add=duration))        #"source pod id: "+str(id_podcast)
        return data_set

    def get_more_by_id(self, get_id):
        storage = Episode.objects.all().values()
        for el in storage:
            if str(el['id'])==get_id:
                link = el['media_link']
                date_add = el['date_add']
                return [link, date_add]
        return None


class Get_playlist:
    def get_setdata_by_id(self, get_id):
        storage = Group_episodes.objects.select_related('id_episode__id_podcast')
        data_set = []
        for el in storage:
            if str(el.id_group.id)==str(get_id):
                id = el.id_episode.id
                name = el.id_episode.name
                id_podcast = el.id_episode.id_podcast.id
                duration = ''
                data_set.append(El_episode(type=El_episode.__name__, id=id, title=name, descr='', add=duration))        #"source pod id: "+str(id_podcast)
        return data_set


class Set_user:
    def create(self, name, passw, rights, date_add):
        usr = User(name=name, password=passw, rights=rights, date_add=date_add)
        if usr is not None:
            usr.save()
            return usr.id
        return False



class Get_author:
    id = 0
    name = ''
    id_user = 0
    date_add = ''

class Get_podcast:
    id = 0
    name = ''
    authors = []
    date_add = ''
    date_add_last = ''

class Get_rating:
    id = 0
    num_likes = 0
    num_views = 0