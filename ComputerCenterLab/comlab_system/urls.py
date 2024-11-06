from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('nav/', views.navigation, name='navigation'),
    path('logout/', views.logout_user, name='logout_user'),
    path('lab_dashboard/', views.lab_dashboard_view, name='lab_dashboard_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('dashboard/lab/<int:lab_id>/', views.dashboard_view, name='dashboard_lab'),
    path('update_status/', views.update_status, name='update_status'),
    path('update_status/dashboard/lab/<int:lab_id>/', views.dashboard_view, name='dashboard_lab'),
    path('add-unit/', views.add_unit, name='add_unit'), 

]
