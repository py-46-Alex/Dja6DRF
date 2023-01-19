"""smart_home URL Configuration
:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime

def time_view(request):
    current_data = datetime.date.today()
    cur_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_data} , {cur_time}'
    return HttpResponse(msg)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
    path('', time_view, name='home'),

]
