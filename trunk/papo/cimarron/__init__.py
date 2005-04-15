import new


DEFAULT_SKIN_NAME = 'gtk2'

class config(object):
    def __init__(self, skin_name=DEFAULT_SKIN_NAME):
        global skin
        skin = __import__('papo.cimarron.skins.' + skin_name,
                          globals(), locals(), skin_name)

