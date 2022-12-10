del db.sqlite3
del tenent\migrations\0001_initial.py

python manage.py makemigrations tenent

python manage.py sqlmigrate tenent 0001

python manage.py migrate

set DJANGO_SUPERUSER_USERNAME=admin
set DJANGO_SUPERUSER_PASSWORD=Welcome#123
set DJANGO_SUPERUSER_EMAIL=manyu1994@hotmail.com
python manage.py createsuperuser --noinput


python manage.py runserver
