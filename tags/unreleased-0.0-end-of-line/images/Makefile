IMAGES=$(wildcard *.png)

.all:
	touch $@

.install: $(IMAGES)
	mkdir -p $(IMAGES_CONF)
	cp $(IMAGES) $(IMAGES_CONF)
	touch $@

