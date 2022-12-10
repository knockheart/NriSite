from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from tenent.model.house_type import HouseType


class AvailableHouse(models.Model):
    list_filter = ('house_type', 'location', 'pin_code', 'available_from')

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    house_name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    house_owner = models.CharField(max_length=200)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    pin_code = models.IntegerField()
    contact_number = models.IntegerField()
    contact_email = models.EmailField()
    available_from = models.DateTimeField()
    expected_monthly_rent = models.IntegerField()

    def __str__(self):
        return f"{self.house_name} {self.house_type.name} {self.location}"


class AvailableHouseAdmin(admin.ModelAdmin):
    list_filter = ('house_type', 'location', 'pin_code', 'available_from')
