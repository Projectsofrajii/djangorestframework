from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreationUserForm
from django.shortcuts import render

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('restapiapp:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('restapiapp:home')
            else:
                messages.info(request, 'Incorrect Username or Password ')
        context = {}
        return render(request, 'signin.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('restapiapp:home')
    else:
        form = CreationUserForm()
        context = {'form': form}
        if request.method == 'POST':
            password = request.POST.get('password')
            form = CreationUserForm(request.POST,password)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Registered Successfully..' + user )
            return redirect('authapp:login')
        return render(request, 'signup.html', context)

def resetpass(request):
    return render(request,'password_reset.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Loggedout Successfully..' )
    return redirect('authapp:logout')

