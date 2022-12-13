from django.http import HttpResponse
from django.template import loader

from tenent.model.available_house import AvailableHouse


def index(request):
    template = loader.get_template('header.html')
    context = {
        "latest_available_house_list": AvailableHouse.objects.all()
    }
    return HttpResponse(template.render(context, request))
