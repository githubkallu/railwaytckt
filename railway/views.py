from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.
def nav(request):
    return render(request,'carousel.html')





def Login_customer(request):
    error = False
    error2 = False
    error3 = False
    if request.method == "POST":
        n = request.POST['uname']
        p = request.POST['pwd']
        try:
            user = authenticate(username=n,password=p)
        except:
            error3 = True
        try:

            if user.is_staff:
                login(request,user)
                error2 = True
            elif user:
                login(request, user)
                error=True
        except:
            error3=True



    d = {'error':error,'error2':error2,'error3':error3}
    return render(request,'login_customer.html',d)

def Register_customer(request):
    error = False
    if request.method == "POST":
        n = request.POST['uname']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        a = request.POST['add']
        m = request.POST['mobile']
        g = request.POST['male']
        d = request.POST['birth']
        p = request.POST['pwd']
        user = User.objects.create_user(first_name=f,last_name=l,username=n,password=p,email=e)
        Register.objects.create(user=user,add=a,mobile=m,gender=g,dob=d)
        error = True
    d = {'error':error}
    return render(request,'register_customer.html',d)

def Search_Train(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Add_route.objects.values('route').distinct()
    ase = Asehi.objects.all()
    coun = 0
    error=False
    fare3=0
    count = 0
    count1 = 0
    data1=0
    data2=0
    route1=[]
    route=0
    b_no =[]
    b_no1 =[]
    bhu=0
    if request.method=="POST":
        f = request.POST["fcity"]
        t = request.POST["tcity"]
        da = request.POST["date"]
        data1 = Add_route.objects.filter(route=f)
        data2 = Add_route.objects.filter(route=t)
        for i in data1:
            for j in data2:
                if i.train.train_no==j.train.train_no:
                    route1.append(Add_Train.objects.filter(train_no=i.train.train_no))
        for i in data1:
            fare1=i.fare
            count+=1
            b_no.append(i.train.train_no)
        for i in data2:
            fare2 = i.fare
            count1+=1
            b_no1.append(i.train.train_no)

        fare3 = fare2-fare1
        if fare3<5 and fare3>0:
            fare3 = 5
        elif fare3<0:
            fare3 = fare3*(-1)
        elif fare3==0:
            fare3 = fare3
        route = f+" to "+t
        Asehi.objects.create(fare=fare3,train_name="bus2",date3=da)
        for i in ase:
            coun = coun + 1
            error=True

    d={"data2":data,'route1':route1,'fare3':fare3,"error":error,'coun':coun,'route':route}
    return render(request,'search_train.html',d)


def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'dashboard.html')

def Logout(request):
    logout(request)
    return redirect('nav')



def Add_train(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=False
    if request.method == "POST":
        n = request.POST['busname']
        no = request.POST['bus_no']
        f = request.POST['fcity']
        to= request.POST['tcity']
        de= request.POST['dtime']
        a = request.POST['atime']
        t = request.POST['ttime']
        d = request.POST['dis']
        i = request.FILES['img']
        Add_Train.objects.create(trainname=n,train_no=no,from_city=f,to_city=to,departuretime=de,arrivaltime=a,trevaltime=t,distance=d,img=i)
        error=True
    d={"error":error}
    return render(request,'add_train.html',d)
def view_train(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data=Add_Train.objects.all()
    d={"data":data}
    return render(request,"view_train.html",d)
def add_route(request):
    error=False
    data=Add_Train.objects.all()

    if request.method == "POST":
        b = request.POST['bus']
        r = request.POST['route']
        f= request.POST['fare']
        d = request.POST['dis']

        bus1 = Add_Train.objects.filter(id=b).get()
        Add_route.objects.create(train=bus1,route=r,distance=d,fare=f)
        error = True

    d={"data":data,"error":error}

    return render(request,'add_route.html',d)

def Book_detail(request,coun,pid,route1):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False

    try:
        data = Asehi.objects.get(id=coun)
    except:
        data = None
    data2 = Add_Train.objects.get(id=pid)
    user2 = User.objects.filter(username=request.user.username).get()
    user1 = Register.objects.filter(user=user2).get()
   
    total = 0
    for i in pro:
        if i.status!="set":
            total = total + i.fare
    passenger=0

    if request.method=="POST":
        f = request.POST["name"]
        t = request.POST["age"]
        da = request.POST["gender"]
      
        