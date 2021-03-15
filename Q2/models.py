from django.db import models


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.CharField(max_length=50)
    percentage_full = models.IntegerField()


class Operation(models.Model):
    name = models.CharField(max_length=50)


class Collection(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()
