from django.urls import path
from user import views

urlpatterns = [
    path("home", views.myhome),
    path("about",views.aboutpage),
    path("services",views.servicepage),
    path("contact",views.contactpage, name='x'),
    path("savedata",views.savedata)
]