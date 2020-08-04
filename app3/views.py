from django.shortcuts import render
from app3.models import user

# Create your views here.
def form(request):
    return render(request,"form.html")

def save(request):
    data={
        'name': request.POST.get('name'),
        'email':request.POST.get('email')
    }
    return render(request,"show.html",data)

def create(request):
    user.objects.create(name="xyz", email="xyz@acd.com")
    return render(request,"create.html")

def displayall(request):
    a=user.objects.all()
    data={
        'obj':a
    }
    return render(request,"display.html",data)

def search(request,id):
    print(id)
    a=user.objects.get(pk=1)
    data={
        'obj':a
    }
    return render(request,"search.html",data)

def displayone(request):
    a=user.objects.get()