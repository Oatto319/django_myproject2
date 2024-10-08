from django.urls import path
from . import views

urlpatterns = [
    path("",  views.indexPage, name="index"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contactUs, name="contact"),
    path("card_color/", views.card_color, name="card_color"),
    path("table/", views.teble, name="table-page"),
]