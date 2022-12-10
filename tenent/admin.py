from django.contrib import admin

from tenent.model.available_house import AvailableHouse, AvailableHouseAdmin
from tenent.model.house_type import HouseType

admin.site.register(AvailableHouse, AvailableHouseAdmin)
admin.site.register(HouseType)
