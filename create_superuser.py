from django.contrib.auth.models import User
from django.db import IntegrityError

# getting name,email & password from env variables
DJANGO_SU_NAME = "admin"
DJANGO_SU_EMAIL = "manyu1994@hotmail.com"
DJANGO_SU_PASSWORD = "Welcome#123"

try:
    superuser = User.objects.create_superuser(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD)
    superuser.save()
except IntegrityError:
    print(f"Super User with username {DJANGO_SU_NAME} is already present")
except Exception as e:
    print(e)