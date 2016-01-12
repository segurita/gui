migrations-dev:
	cd gui && python manage.py makemigrations --settings=gui.settings.dev
	cd gui && python manage.py migrate --settings=gui.settings.dev
