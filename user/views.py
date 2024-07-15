
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myhome(request):
   # return HttpResponse("this is my first url hit")
    return render(request,"home.html")

def aboutpage(request):
   # return HttpResponse("THIS IS ABOUT PAGE ")
    return render(request,"about.html")

def servicepage(request):
    return render(request,"services.html")

def contactpage(request):
    return render(request,"contact.html")



#blog----home,about,contact,services