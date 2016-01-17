.PHONY = migrations-dev serve

migrations-dev:
	cd gui && python manage.py makemigrations --settings=gui.settings.dev
	cd gui && python manage.py migrate --settings=gui.settings.dev

serve:
	cd gui && python manage.py runserver --settings=gui.settings.dev
