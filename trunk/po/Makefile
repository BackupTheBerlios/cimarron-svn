
ALL_POS=$(wildcard *.po)
ALL_MOS=$(ALL_POS:%.po=%.mo)

.all: $(ALL_MOS)
	touch $@

messages.pot: $(ALL:%=../%)
	xgettext --output=$@ --copyright-holder="Fundacion Via Libre" --msgid-bugs-address=papo-hackers@nongnu.org --sort-by-file --foreign-user --indent $^

%.po: messages.pot
	msgmerge -U $@ $^
	touch $@

%.mo: %.po
	msgfmt -o$@ $^

.install: .all
	mkdir -p $(LOCALES_CONF)
	for i in $(ALL_MOS); do TARGET=$(LOCALES_CONF)/`basename $$i .mo`/LC_MESSAGES/; mkdir -p "$$TARGET"; cp --backup=t "$$i" "$$TARGET/cimarron.mo"; done
