from django.contrib import admin
from django.urls import path
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetEvents, name='event_list'),
    path('event/<int:id>/', views.GetEvent, name='event_url'),
    path('page-delete/<int:id>', views.DeleteEvent, name='delete_event'),
]
