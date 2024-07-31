
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
        img=request.FILES.get("myimg")
       # print(fullname,email,msg)
    data=contactUs( fullname= fullname, email=email,message=msg,saveimg=img)
    data.save()

    return redirect('x')
    


def deletefata(request, x):
    q = contactUs.objects.get(id = x)
    q.delete()
    return redirect('y')
    # return HttpResponse("DATA IS delete SUCESS")
    # pass

def updatedata(request,abc):
    obj=contactUs.objects.get(id=abc)
    return render(request,"updatedata.html",{"record":obj})
    return redirect("y")

def datarecord(request,abc):
    obj=contactUs.objects.get(id=abc)
    if request.method=="POST":
        fullname=request.POST.get('fname')
        email=request.POST.get('email')
        msg=request.POST.get("msg")

       #objname.coliumn=new_data 
        obj.fullname=fullname
        obj.email=email
        obj. message=msg

        obj.save()
    return redirect("y")


def searching(request):
    #pass
    query=request.GET.get("q")
   #ORM WO DATA JO SEARCH HO RHA
    #MODEL NAME(modals wali file se).OBJECTS.FILTR
    if query:
        xyz=contactUs.objects.filter(fullname__icontains=query) | contactUs.objects.filter( email__icontains=query)
        return  render(request,"about.html", {"my_data":xyz})

    else:
        all_records=contactUs.objects.all()
        return render(request,"about.html",{"my_data":all_records})
#blog----home,about,contact,services