## Run 

`python manage.py runserver`

## Migrate DB

`python manage.py makemigrations tenent`

`python manage.py sqlmigrate tenent 0001`

`python manage.py migrate`

## Super User

`python manage.py createsuperuser`

`python manage.py shell < mysite/create_superuser.py`

```
set DJANGO_SUPERUSER_USERNAME=admin
set DJANGO_SUPERUSER_PASSWORD=Welcome#123
set DJANGO_SUPERUSER_EMAIL=manyu1994@hotmail.com
python manage.py createsuperuser --noinput
```