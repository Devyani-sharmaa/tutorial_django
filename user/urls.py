from django.urls import path
from user import views

urlpatterns = [
    path("home", views.myhome),
    path("about",views.aboutpage, name="y"),
    path("services",views.servicepage),
    path("contact",views.contactpage, name='x'),
    path("savedata",views.savedata),
    path("delte-record/<int:x>",views.deletefata),
    path("update-record/<int:abc>",views.updatedata),
    path("updatedata/<int:abc>",views.datarecord),
     path("search-record",views.searching)
]   