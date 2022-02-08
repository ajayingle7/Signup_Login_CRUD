from django.shortcuts import render,redirect
from .forms import ProfileForm,OrderForm
from .models import Profile,Order
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def profileView(request):
    template_name = 'app1/profileview.html'
    form = ProfileForm()

    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()




    context ={'form':form}
    return render(request,template_name,context)

@login_required()
def orderView(request):
    template_name = 'app1/orderview.html'
    form = OrderForm()

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,template_name,context)

@login_required()
def profileData(request):
    template_name = 'app1/profiledata.html'
    obj = Profile.objects.all()

    context = {'data':obj}
    return render(request,template_name,context)


def updateView(request,id):
    template_name = 'app1/profileview.html'
    obj = Profile.objects.get(pid=id)
    form = ProfileForm(instance=obj)

    if request.method=='POST':
        form = ProfileForm(request.POST,instance=obj)
        form.save()

        return redirect('profiledata')

    context = {'form':form}
    return render(request,template_name,context)


def deleteView(request,id):
    template_name = 'app1/confirm.html'
    obj = Profile.objects.get(pid = id)


    if request.method=='POST':
        obj.delete()

        return redirect('profiledata')

    context = {'data':obj}

    return render(request,template_name,context)
