from django.contrib.auth.models import User
from django.db import models


class HouseType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
