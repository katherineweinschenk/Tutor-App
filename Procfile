release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn SuperTuber.wsgi --log-level debug
