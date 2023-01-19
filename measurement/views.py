# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, \
    ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSeriaizer, SensorDetailSerializer, PostSerialier, SensorSeriaizerforCreatin, \
    SensorSeriaizerChanger, MeshAddCreate


# @api_view(['GET'])
# def sensors(request):
#     sensors = Sensor.objects.all()
#     ser = SensorSeriaizer(sensors, many=True)
#     return Response(ser.data)

class SensorView(APIView):
    def get(self, request):
        rr = Sensor.objects.all()
        seri = SensorSeriaizer(rr, many=True)
        return Response(seri.data)

    def post(self, request):
        serializer = SensorSeriaizerforCreatin(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'DaT4uK': serializer.data})
#
class OnesensorView(RetrieveUpdateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
#
class CreateSensor(CreateAPIView):

    serializer_class = PostSerialier
    queryset = Sensor.objects.all()

    def post(self, request, *args, **kwargs):
       return self.get(request, *args, **kwargs)
#
class Addmeashure(ListCreateAPIView):

    serializer_class = MeshAddCreate
    queryset = Measurement.objects.all()
