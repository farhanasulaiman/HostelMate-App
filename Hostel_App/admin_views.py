from _multiprocessing import recv
from django.shortcuts import render, redirect

from Hostel_App.forms import StudForm
from Hostel_App.models import Student, Parent


# view student list
def view_stud(request):
    data = Student.objects.all()
    return render(request, "admin/view_stud.html", {"data": data})


# delete student record
def del_stud(request, id):
    if request.method == "POST":
        record = Student.objects.get(id=id)
        user1 = record.user
        record.delete()
        user1.delete()
        return redirect('viewstud')
    return render(request, "admin/view_stud.html")


# update student record
def updt_stud(request, id):
    record = Student.objects.get(id=id)
    stud_form = StudForm(instance=record)
    if request.method == "POST":
        stud_form1 = StudForm(request.POST, request.FILES, instance=record)
        if stud_form1.is_valid():
            stud_form1.save()
            return redirect('viewstud')
        else:
            stud_form = stud_form1
    return render(request, 'admin/updt_stud.html', {"stud_form": stud_form})


# view parent list
def view_par(request):
    data = Parent.objects.all()
    return render(request, 'admin/view_parent.html', {"data": data})


# delete parent record
def del_par(request, id):
    if request.method == "POST":
        record = Parent.objects.get(id=id)
        user1 = record.user
        record.delete()
        user1.delete()
        return redirect('viewpar')
    return redirect(request, 'admin/view_par.html')
