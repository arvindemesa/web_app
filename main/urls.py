from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('Dashboard', views.view_dashboard, name='view-dashboard'),
    path('Dashboard/RefreshCPU', views.refresh_cpu, name='refresh-cpu'),
]