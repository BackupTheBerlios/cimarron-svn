
ALL=$(wildcard src/cimarron.py src/Generic/*.py src/Gtk2/*.py)
export ALL

TAGS: $(ALL)
	etags $^

all: .all

install: .install

reinstall:
	find -name .install -print0 | xargs -r -0 rm -v
	$(MAKE) install

.all: $(ALL)
	$(MAKE) -C po .all

.config: src/cimarron.cfg
	PYTHONPATH=src:$(PYTHONPATH) python -c 'f=file("$@", "w");from Utils.Parser import Parser; p=Parser(); p.readfp(file("$^")); [f.write("%s=%s\nexport %s\n" % (K, p.getlist("DEFAULT", k)[0], K)) for k, K in [(i, i.upper()+"_CONF") for i in ("locales","images","shared","prefix","config_files")]]' || rm .config

-include .config

.install:
	$(MAKE) -C po .install
	$(MAKE) -C images .install
	$(MAKE) -C src .install
	touch $@
