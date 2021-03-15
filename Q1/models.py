from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=50)


class NavigationRecord(models.Model):
    vehicle= models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    datetime = models.DateTimeField(db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(str(self.vehicle.plate), self.datetime, self.latitude, self.longitude)


