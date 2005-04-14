all:

clean:

distclean: clean
	find '(' -name '*.py[co]' -o -name '*~' ')' -print0 | xargs -0 -r rm -v

test:
	echo $(TESTOPTS)
	PYTHONPATH=.:$$PYTHONPATH python tests/run.py

install:
	
