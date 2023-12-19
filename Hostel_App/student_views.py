from django.shortcuts import render

from Hostel_App.models import Weekly_Foods


# view weekly food
def view_weekly_food(request):
    data = Weekly_Foods.objects.filter().order_by('id')          # view the data based on id ascending order
    return render(request, 'student/view_weekly_food.html', {"data": data})
