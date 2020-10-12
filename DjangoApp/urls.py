from django.urls import path
# from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.loginuser, name='loginuser'),
    path('signup/',views.signupuser,name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('<int:field1>/', views.detail, name='detail'),
    path('home/', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('listview', views.ListView.as_view(), name='listview'),
    path('addnotes/', views.FormView.as_view(), name='formview'),
    path('viewnotes/', views.view_notes, name='view_notes'),
    path('viewnotes/delete/<int:noteid>/', views.delete_notes, name='delete_notes'),
    path('viewnotes/edit/<int:noteid>/', views.edit_notes, name='edit_notes'),
    # path('add/',TemplateView.as_view(template_name="add.html"))
]