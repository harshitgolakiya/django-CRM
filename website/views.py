from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm, RecordForm
from .models import Record
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def homeview(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'welcome {username},logged in successfully')
            return showdata(request)
        else:
            messages.info(request,'invalid credentials')
            return render(request,'home.html')
    else:
        return showdata(request)
    
def showdata(request):
    record = Record.objects.all()
    return render(request,'home.html',{'record':record})

    
def logoutview(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('home')
# Create your views here.
def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f'welcome {username},account created successfully')
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

def recordview(request,pk):
    # return render(request,'record.html')
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        print(record)
        return render(request,'record.html',{'record':record})
    else:
        return redirect('home')

def deleterecord(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        return redirect('home')
    else:
        return redirect('home')
    


@login_required(login_url='home')
def addrecord(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecordForm()
    
    return render(request, 'addrecord.html', {'form': form})

@login_required(login_url='home')
def updaterecord(request,pk):
    
    record = get_object_or_404(Record, id=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful update
    else:
        form = RecordForm(instance=record)
    
    return render(request, 'addrecord.html', {'form': form})

# @login_required(login_url='home')
# def updaterecord(request,pk):       
#     if request.method == 'POST':
#         record = Record.objects.get(id=pk)
#         form = RecordForm(request.POST,instance=record)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         record = Record.objects.get(id=pk)
#         form = RecordForm(instance=record)

#     return render(request, 'addrecord.html', {'form': form})