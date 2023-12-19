from django.shortcuts import render, redirect

from Hostel_App.forms import StudForm, WeeklyFoodForm, NotificationForm
from Hostel_App.models import Student, Parent, Weekly_Foods, Notifications


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


# weekly food managing view
def add_weekly_food(request):
    food_form = WeeklyFoodForm()
    if request.method == 'POST':
        food_form1 = WeeklyFoodForm(request.POST)
        if food_form1.is_valid():
            food_form1.save()
        else:
            food_form = food_form1
    return render(request, 'admin/add_weekly_food.html', {"food_form": food_form})


# view weekly food
def view_weekly_food(request):
    data = Weekly_Foods.objects.filter().order_by('id')  # view the data based on id ascending order
    return render(request, 'admin/view_weekly_food.html', {"data": data})


# update weekly food
def updt_weekly_food(request, id):
    record = Weekly_Foods.objects.get(id=id)
    updt_form = WeeklyFoodForm(instance=record)
    if request.method == 'POST':
        updt_form1 = WeeklyFoodForm(request.POST, instance=record)
        if updt_form1.is_valid():
            updt_form1.save()
            return redirect('viewfood')
        else:
            updt_form = updt_form1
    return render(request, 'admin/updt_weekly_food.html', {"updt_form": updt_form})


# add notification
def add_notification(request):
    notif_form = NotificationForm()
    if request.method == 'POST':
        notif_form1 = NotificationForm(request.POST)
        if notif_form1.is_valid():
            notif_form1.save()
        else:
            notif_form = notif_form1
    return render(request, 'admin/add_notification.html', {"notif_form": notif_form})


# view notification
def view_notification(request):
    data = notifications = Notifications.objects.filter().order_by('-date')[:3]
    return render(request, 'admin/view_notification.html', {"data": data})


# view all notification
def all_notification(request):
    data = notifications = Notifications.objects.filter().order_by('-date')
    return render(request, 'admin/view_notification.html', {"data": data})


# delete notification
def delete_notification(request, id):
    if request.method == 'POST':
        record = Notifications.objects.get(id=id)
        record.delete()
        return redirect('viewnotif')
    return render(request, 'admin/view_notification.html')


# update notification
def updt_notification(request, id):
    record = Notifications.objects.get(id=id)
    updt_form = NotificationForm(instance=record)
    if request.method == 'POST':
        updt_form1 = NotificationForm(request.POST, instance=record)
        if updt_form1.is_valid():
            updt_form1.save()
            return redirect('viewnotif')
        else:
            updt_form = updt_form1
    return render(request, 'admin/updt_notification.html', {"updt_form": updt_form})
