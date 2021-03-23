from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_dashboard, name='dashboard'),
    path('<str:username>', views.user_dashboard, name='dashboard'),
    path('history/<str:username>', views.user_history_dashboard, name='dashboard'),
    path('files/<str:username>', views.userFilesDashboard, name='dashboard')
]