from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import items
from .models import Guser
# Create your views here.
def home(request):
    return render(request,'home.html',{'already':False,'wrong':False})

def register(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        users=Guser.objects.all().filter(username=username)
        if users:
            return render(request,'home2.html',{'already':True,'wrong':False})
        else:
            g=Guser(username=username,password=password)
            g.save()
            return render(request,'userlist.html',{'items':[],username:username})
    else:
        return render(request,'home2.html',{'already':False,'wrong':False})
def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            users=Guser.objects.get(username=username,password=password)
        except:
            return  render(request,'home.html',{'already':False,'wrong':True})
        itemss=items.objects.all().filter(username=username)
        return render(request,'userlist.html',{'items':itemss,'username':username})
    else:
        return render(request,'home.html',{'already':False,'wrong':False})

def search(request,username):
    itemss=items.objects.all().filter(username=username,date=request.POST['date'])
    print(username)
    return render(request,'userlist.html',{'items':itemss,'username':username})
def add(request,username):
    if request.method == 'GET':
        return render(request,'add.html',{'username':username})
    else:
        users=Guser.objects.all().filter(username=username)
        i=items(username=users[0],name=request.POST['name'],quantity=request.POST['quantity'],status=request.POST['status'],date=request.POST['date'])
        i.save()
        itemss=items.objects.all().filter(username=username)
        return render(request,'userlist.html',{'items':itemss,'username':username})