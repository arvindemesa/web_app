from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.view_dashboard, name='view-homepage'),
    path('Main/', include('main.urls')),
    path('admin/', admin.site.urls),
]
