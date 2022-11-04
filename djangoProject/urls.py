from django.contrib import admin
from django.urls import path
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetEvents),
    path('event/<int:id>/', views.GetEvent, name='event_url'),
]
