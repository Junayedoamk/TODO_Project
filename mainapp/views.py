from django.shortcuts import render, HttpResponseRedirect
from mainapp.forms import CustomUserCreationForm, TodoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TODO


# Create your views here.


def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']  
            user = authenticate(email = email, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/todolist/')
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form':form})

def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='login')
def todolist(request):
    if request.user.is_authenticated:
        user = request.user
        todos = TODO.objects.filter(user = user)
        return render(request, 'todolist.html', {'todos':todos})

@login_required(login_url='login')
def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return HttpResponseRedirect('/todolist/')
        else: 
            form = TodoForm
            return render(request , 'addtodo.html' , context={'form' : form})

def delete_todo(request , id ):
    TODO.objects.get(pk = id).delete()
    return HttpResponseRedirect('/todolist/')

def change_todo(request, id, status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return HttpResponseRedirect('/todolist/')
