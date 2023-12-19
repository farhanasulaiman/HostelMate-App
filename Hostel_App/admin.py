from django.contrib import admin

from Hostel_App import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Parent)
admin.site.register(models.Weekly_Foods)
admin.site.register(models.Notifications)
