from django.shortcuts import render,redirect
from .models import Register

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'home/index.html')
    else:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        r=Register(username=username,email=email,password=password)
        r.save()
        return render(request,'home/index.html',{'msg':'User Registration Successfully !'})


def login(request):
    if request.method == 'GET':
        return render(request,'home/login.html')
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['user']=request.POST['username']
        r=Register.objects.filter(username=username,password=password)
        if r:
            return redirect('profile')
        else:
            return render(request,'home/login.html',{'msg':'Invalid Username or Password!'})
        

def profile(request):
    userdata=request.session.get('user')
    if userdata is not None:
        return render(request,'home/profile.html',{'userdata':userdata})
    else:
        return redirect('login')


def logout(request):
    del request.session['user']
    return redirect('login')
