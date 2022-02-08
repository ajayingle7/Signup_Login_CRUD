from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def signupView(request):
    template_name = 'app2/signup.html'
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()




    context = {'form':form}

    return render(request,template_name,context)



def loginView(request):
    template_name = 'app2/login.html'
    context  ={}

    if request.method=='POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        user = authenticate(username=un, password=pw)

        if user is not None:
            login(request,user)

            return redirect('profileview')




    return render(request,template_name,context)



def logutView(request):
    logout(request)

    return redirect('login')