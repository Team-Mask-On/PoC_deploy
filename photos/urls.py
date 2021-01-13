from django.urls import path
from . import views

app_name = "photos"
urlpatterns = [
    path("send", views.ReceptPhoto.as_view(), name="send")
]