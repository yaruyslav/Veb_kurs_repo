from .table_interfaces import *
from .storage_classes import *
import random


class Rec_service:
    def get_all_episodes(self):
        set_data = Get_episode().get_Episodes_By_Command("all")
        return set_data
    
    def get_rand_episodes(self, num):
        set_data = Get_episode().get_Episodes_By_Command("all")
        aviable_elem = set_data.copy()
        new_data = []
        for i in range(len(aviable_elem)):
            ind = random.randint(0, len(aviable_elem)-1)
            el = aviable_elem.pop(ind)
            new_data.append(el)
            if i+1 >= num:
                break
        return new_data

class Sorter:
    id = 0

class Search_service:
    def search_by_name(self, type, name):
        set_data = Get_episode().get_Episodes_By_Command("all")
        ret_data = []
        for el in set_data:
            if el['name']==name:
                ret_data.append(el)
        return ret_data()