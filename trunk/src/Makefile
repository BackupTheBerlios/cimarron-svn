
ALL=$(wildcard cimarron.py */*.py)
ALL_POS=po/*.po

pos: $(ALL_POS:%.po=%.mo)

TAGS: $(ALL)
	etags $^

.install: $(ALL)
	mkdir -p $(PREFIX_CONF)
	cp --parents $(ALL) $(PREFIX_CONF)
	mkdir -p $(dir $(CONFIG_FILES_CONF))
	cp cimarron.cfg $(CONFIG_FILES_CONF)
	touch $@
