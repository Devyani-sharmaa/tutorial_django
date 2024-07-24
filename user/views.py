
from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import contactUs

# Create your views here.
def myhome(request):
   # return HttpResponse("this is my first url hit")
    return render(request,"home.html")

def aboutpage(request):
    y=contactUs.objects.all()
    print(y)
   # return HttpResponse("THIS IS ABOUT PAGE ")
    return render(request,"about.html",{"my_data":y})

def servicepage(request):
    return render(request,"services.html")

def contactpage(request):
    return render(request,"contact.html")


def savedata(request):
    if request.method=="POST":
        fullname=request.POST.get('fname')
        email=request.POST.get('email')
        msg=request.POST.get("msg")
       # print(fullname,email,msg)
    data=contactUs( fullname= fullname, email=email,message=msg)
    data.save()

    return redirect('x')
    


def deletefata(request, x):
    q = contactUs.objects.get(id = x)
    q.delete()
    return redirect('y')
    # return HttpResponse("DATA IS delete SUCESS")
    # pass

def updatedata(request,u):
    p=contactUs.objects.get(id=u)
    p.update()
    return redirect("y")

#blog----home,about,contact,services