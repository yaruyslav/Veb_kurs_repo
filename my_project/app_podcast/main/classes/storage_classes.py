
class User_data:
    def __init__(self, name, passw, rights, id, group_arr=0):
        if group_arr:
            self.group_arr = []
        self.id = id
        self.name = name
        self.password = passw
        self.rights = rights

class Admin_data:
    def __init__(self, name, passw, rights, id, group_arr=0):
        if group_arr:
            self.group_arr = []
        self.id = id
        self.name = name
        self.password = passw
        self.rights = rights

class Usr_group:
    def __init__(self, id, name, id_usr):
        self.id = id
        self.name = name
        self.id_user = id_usr

class El_episode:
    def __init__(self, type, id, title='', descr='', add=''):
        self.type = type
        self.id = id
        self.title = title
        self.description = descr
        self.addition = add



class El_podcast:
    type = ''
    id = 0
    title = ''
    description = ''
    addition = ''
    def __init__(self, type, id, title='', descr='', add=''):
        self.type = type
        self.id = id
        self.title = title
        self.description = descr
        self.addition = add

class El_author:
    type = ''
    id = 0
    title = ''
    def __init__(self, type, id, title=''):
        self.type = type
        self.id = id
        self.title = title

class El_playlist:
    type = ''
    id = 0
    title = ''
    addition = ''
    def __init__(self, type, id, title='', add=''):
        self.type = type
        self.id = id
        self.title = title
        self.addition = add

class El_other:
    type = ''
    id = 0
    title = ''
    description = ''
    addition = ''
    def __init__(self, type, id, title='', descr='', add=''):
        self.type = type
        self.id = id
        self.title = title
        self.description = descr
        self.addition = add



class Item_group:
    id = 0
    type_data = 0
    name = ''
    array = []
    sort_type = 0