from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import login  , logout, authenticate
from .forms import registration
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid:
            form.save()
            return redirect('accounts:login')
    else:
        form = registration()

    return render(request , "accounts/register.html" , {'form':form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Showroom:brand_list')
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {'form': form})
def logout_view(request):
    logout (request)
    return redirect('accounts:login')

def Delete_account(requsest):
    requsest.user.delete()
    messages.success(requsest , "Your account has been deleted!")
    return redirect('accounts:login')