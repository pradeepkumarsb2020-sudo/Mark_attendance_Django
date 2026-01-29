from django.urls import path
from .import views
urlpatterns=[
    path('',views.student_list,name='students'),
    path('mark/',views.mark_attendance,name='mark_attendance'),
    path('records/',views.attendance_list,name='attendance_list')
]