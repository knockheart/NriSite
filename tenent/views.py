from django.views.generic import ListView
from tenent.model.available_house import AvailableHouse


class PublisherListView(ListView):
    model = AvailableHouse
    template_name = "house_list.html"
