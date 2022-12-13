from django.urls import path

from .views import PublisherListView

urlpatterns = [
    path('', PublisherListView.as_view()),
]
