import new
import libxml2

DEFAULT_SKIN_NAME = 'gtk2'

class config(object):
    def __init__(self, skin_name=DEFAULT_SKIN_NAME):
        global skin
        skin = __import__('papo.cimarron.skins.' + skin_name,
                          globals(), locals(), skin_name)


def fromXmlObj(xmlObj, parent=None):
    if isinstance(xmlObj, libxml2.xmlDoc):
        # get at root element
        xmlObj = xmlObj.children
    obj = getattr(skin, xmlObj.name)()
    prop = xmlObj.properties
    while prop:
        setattr(obj, prop.name, eval(prop.content))
        prop = prop.next
    if parent is not None:
        obj.parent = parent
    xmlObj = xmlObj.children
    while xmlObj:
        fromXmlObj(xmlObj, parent=obj)
        xmlObj = xmlObj.next
            
    return obj
