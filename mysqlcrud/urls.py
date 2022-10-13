from django.urls import path
from .import views

urlpatterns=[
    path('',views.LoadForm),
    path('display',views.DisplayForm),
    path('',views.LoadStudentForm),
    path('insert',views.InsertStudent),
    path('show',views.DisplayStudent),
    path('delete/<int:sid>',views.DeleteStudent,name='delete'),
    path('edit/<int:sid>', views.EditStudent, name='edit'),
    path('update/<int:sid>',views.UpdateStudent)

]