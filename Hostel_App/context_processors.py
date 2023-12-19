# view notification
def view_notification(request):
    # lazy importing
    # import statements if given first may directly or indirectly lead to the use of Django models
    from Hostel_App.models import Notifications
    notifications = Notifications.objects.filter().order_by('-date')
    return {"notifications": notifications}

# delete notification
# def del_notification(request):
#     from Hostel_App.models import Notifications
#     if request.method == 'POST':
#         id = request.POST['btn_delete']
#         record = get_object_or_404(Notifications,id=id)
#         record.delete()
#     notifications = Notifications.objects.filter().order_by('-date')
#     return {"notifications": notifications}
