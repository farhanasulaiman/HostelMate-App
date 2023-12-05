from django.urls import path

from Hostel_App import views, admin_views

urlpatterns = [
    path('', views.view, name="index"),
    path('myadmin', views.view_admin, name="myadmin"),
    path('student', views.view_stud, name="student"),
    path("parent", views.view_parent, name="parent"),
    path("mylogin", views.login_view, name="mylogin"),
    path("studreg", views.stud_register, name="studreg"),
    path("parentreg", views.parent_register, name="parentreg"),
    path("viewstud", admin_views.view_stud, name="viewstud"),
    path("delstud/<int:id>/", admin_views.del_stud, name="delstud"),
    path("updtstud/<int:id>/", admin_views.updt_stud, name="updtstud"),
    path("viewpar", admin_views.view_par, name="viewpar"),
    path("delpar/<int:id>/", admin_views.del_par, name="delpar")
]
