
simple_types = (str, unicode, type(None), bool, int, long, float, complex )

def is_simple(obj):
    t = type(obj)

    return (t in simple_types # really simple
            or ( t in (tuple, list) and 
                 len(filter(None, map(is_simple, obj))) == len(obj)) # composite of simples
            or ( t is dict and
                 len(filter(None, map(is_simple, obj.keys()))) == \
                 len(filter(None, map(is_simple, obj.values()))) == len(obj))
            )
                 
