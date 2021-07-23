from django.http.response import HttpResponse
from django.shortcuts import render
from user.models import User,Post


# Create your views here.
def index(request):
    return render(request,'index.html')

def user(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = User(firstname= firstname,lastname=lastname,email=email,password=password,username=username)
        user.save()
        
    return render(request,'user.html')
def Post(request):
    if request.method == "POST":
        postUser= request.POST.get('postUser')
        text = request.POST.get('text')
        createdat = request.POST.get('createdat')
        updatedat = request.POST.get('updatedat')
        post = Post(postUser=postUser,text=text,createdat=createdat,updatedat=updatedat)
        post.save()
        
    return render(request,'post.html')
    
    


    