from django.contrib import admin
from django.contrib import admin
from django.urls import path
from home import views



urlpatterns = [
    path("photo/",views.photo,name="photo"),
    path("contact/",views.contact,name="contacts"),
    path("creator_contact/",views.creator_contact,name="creator_contact"),

]