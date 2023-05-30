from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    legs = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
