from django.contrib import admin
from django.urls import path
from bmstu_lab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetCities),
    path('city/<int:id>/', views.GetCity, name='city_url'),
]
