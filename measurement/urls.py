from django.urls import path
# from measurement.views import SensorView
from measurement.views import OnesensorView, CreateSensor, SensorView, Addmeashure

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', OnesensorView.as_view()),
    path('measurements/', Addmeashure.as_view())
]
    #
#     http://127.0.0.1:8000/api/sensors/
