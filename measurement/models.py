from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    # measurements
#
class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=6, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, null=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    pictures = models.ImageField(max_length=None, null=True)

#
