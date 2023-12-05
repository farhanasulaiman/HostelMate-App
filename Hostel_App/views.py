from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Hostel_App.forms import LoginForm, StudForm, ParentForm


# Create your views here.
# view landing page
def view(request):
    return render(request, "index.html")


# view admin page
def view_admin(request):
    return render(request, "base/admin_home.html")


# view student page
def view_stud(request):
    return render(request, "base/student_home.html")


# view parent page
def view_parent(request):
    return render(request, "base/parent_home.html")


# Student Registration
def stud_register(request):
    stud_form = StudForm()
    log_form = LoginForm()

    if request.method == 'POST':
        stud_form = StudForm(request.POST, request.FILES)
        log_form = LoginForm(request.POST)
        if stud_form.is_valid() and log_form.is_valid():
            log1 = log_form.save(commit=False)
            log1.is_student = True
            log1.save()
            stud1 = stud_form.save(commit=False)
            stud1.user = log1
            stud1.save()
            stud_form = StudForm()
            log_form = LoginForm()
            return redirect('mylogin')
    return render(request, "stud_register.html", {"log_form": log_form, "stud_form": stud_form})


# Parent Registration

def parent_register(request):
    par_form = ParentForm()
    log_form = LoginForm()
    if request.method == 'POST':
        par_form = ParentForm(request.POST)
        log_form = LoginForm(request.POST)
        if par_form.is_valid() and log_form.is_valid():
            log1 = log_form.save(commit=False)
            log1.is_parent = True
            log1.save()
            par1 = par_form.save(commit=False)
            par1.user = log1
            par1.save()
            par_form = ParentForm()
            log_form = LoginForm()
            return redirect('mylogin')
    return render(request, "parent_register.html", {"log_form": log_form, "par_form": par_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('myadmin')
            elif user.is_student:
                return redirect('student')
            elif user.is_parent:
                return redirect('parent')
        else:
            messages.error(request, "Invalid Credentials!")
        username = ""
        password = ""
    return render(request, "login.html")
