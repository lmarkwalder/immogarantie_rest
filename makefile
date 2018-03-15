install:
	pip3 install -r requirements.txt
	virtualenv -p python3 $(shell pwd)/venv
	cd $(shell pwd) && export FLASK_APP=run.py && flask db upgrade

tests:
	cd $(shell pwd) && nosetests --traverse-namespace test


run:
	cd $(shell pwd) && export FLASK_APP=run.py && source venv/bin/activate && flask run

.PHONY: install, tests, run
