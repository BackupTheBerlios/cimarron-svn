from Utils.MagicArgs import MagicArgs
from Exceptions import ConfigError

def _(s):
    raise Exception, "You **PILLOCK**!! You broke something!"

class Config(MagicArgs):
    def setConfig(klass, config):
        klass.__config = config
    setConfig = classmethod(setConfig)

    def getConfig(klass, key, default, which, empty=None):
        """
        getConfig() is a class method that returns configuration
        values. It looks up the value along the MRO of the class.

        All the getConfigAsFoo methods return the appropriate type of
        object (if at all possible).
        """
        try:
            val = klass.__config_dict.get(key, None)
        except AttributeError:
            klass.__config_dict = {}
            val = None
        if val is None:
            for i in klass.mro():
                try:
                    val = getattr(klass.__config, which)(i.__name__, key)
                    if val: break
                except:
                    pass
            if val is None:
                val = empty
            klass.__config_dict[key] = val
        if val is None:
            if default is not None:
                val = default
            else:
                raise ConfigError, _("Unable to find value for configuration key `%s'") % (key,)
        return val
    getConfig = classmethod(getConfig)

    def getConfigAsString(klass, key, default=None):
        return klass.getConfig(key, default, "get")
    getConfigAsString = classmethod(getConfigAsString)

    def getConfigAsList(klass, key, default=None):
        return klass.getConfig(key, default, "getlist")
    getConfigAsList = classmethod(getConfigAsList)

    def getConfigAsNum(klass, key, default=None):
        return klass.getConfig(key, default, "getint")
    getConfigAsNum = classmethod(getConfigAsNum)

    def getConfigAsFloat(klass, key, default=None):
        return klass.getConfig(key, default, "getfloat")
    getConfigAsFloat = classmethod(getConfigAsFloat)

    def getConfigAsBoolean(klass, key, default=None):
        return klass.getConfig(key, default, "getboolean")
    getConfigAsBoolean = classmethod(getConfigAsBoolean)

