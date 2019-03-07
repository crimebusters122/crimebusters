from django.db import models

class LocationType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    loc_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class VariableType(models.Model):
    loc_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Variable(models.Model):
    var_type = models.ForeignKey(VariableType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name