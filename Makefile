.PHONY = migrations-dev import-data-dev serve

migrations-dev:
	cd gui && python manage.py makemigrations --settings=gui.settings.dev
	cd gui && python manage.py migrate --settings=gui.settings.dev

import-data-dev:
	cd gui && python manage.py import_data --folder ../../data/data --settings=gui.settings.dev

serve:
	cd gui && python manage.py runserver --settings=gui.settings.dev
