from django.shortcuts import render,redirect
from .forms import Signup_form

def signup(request):
    if request.method=="POST":
        form=Signup_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/game')
            except:
                pass
    else:
        form=Signup_form()        
    return render(request,'index.html',{'form':form})

def game(request):
    return render(request,'game.html')

# Create your views here.
