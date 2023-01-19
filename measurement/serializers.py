from rest_framework import serializers
from measurement.models import Sensor, Measurement

class SensorSeriaizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
#
class SensorSeriaizerChanger(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ("id", 'description')


    def partial_update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
#
# class SensorSeriaizer(serializers.Serializer):
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name']
class Mesha(serializers.Serializer):
    temperature = serializers.DecimalField(max_digits=5, decimal_places=1)
    created_at = serializers.DateTimeField()
    pictures = serializers.ImageField()



class MeasurementSerializer(serializers.Serializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'pictures']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = Mesha(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

class PostSerialier(serializers.ModelSerializer):
    class Meta:
            model=Sensor
            fields = ['name', 'description']
#
class MeshAddCreate(serializers.ModelSerializer):
    class Meta:
            model=Measurement
            fields = ['sensor', 'temperature']
#
class SensorSeriaizerforCreatin(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)




