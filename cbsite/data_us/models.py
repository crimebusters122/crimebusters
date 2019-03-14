from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class LocationType1(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location1(models.Model):
    location_type_1 = models.ForeignKey(LocationType1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VariableType1(models.Model):
    location_type_1 = models.ForeignKey(LocationType1, on_delete=models.CASCADE)
    variable_type_1 = models.CharField(max_length=100)

    def __str__(self):
        return self.variable_type_1

class VariableChoices1(models.Model):
    location_type_1 = models.ForeignKey(LocationType1, on_delete=models.CASCADE)
    location_1 = models.ForeignKey(Location1, on_delete=models.CASCADE)
    variable_type_1 = models.ForeignKey(VariableType1, on_delete=models.CASCADE)
    variable_1 = models.CharField(max_length=200)

class LocationType2(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location2(models.Model):
    location_type_2 = models.ForeignKey(LocationType2, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VariableType2(models.Model):
    location_type_2 = models.ForeignKey(LocationType2, on_delete=models.CASCADE)
    variable_type_2 = models.CharField(max_length=100)

    def __str__(self):
        return self.variable_type_2

class VariableChoices2(models.Model):
    location_type_2 = models.ForeignKey(LocationType2, on_delete=models.CASCADE)
    location_2 = models.ForeignKey(Location2, on_delete=models.CASCADE)
    variable_type_2 = models.ForeignKey(VariableType2, on_delete=models.CASCADE)
    variable_2 = models.CharField(max_length=200)

class NextPage(models.Model):
    variable_type_1 = models.ForeignKey(VariableType1, on_delete=models.CASCADE)
    location_type_1 = models.ForeignKey(LocationType1, on_delete=models.CASCADE)
    variable_1 = models.ForeignKey(VariableChoices1, on_delete=models.CASCADE)
    location_1 = models.ForeignKey(Location1, on_delete=models.CASCADE)
    variable_type_2 = models.ForeignKey(VariableType2, on_delete=models.CASCADE)
    location_type_2 = models.ForeignKey(LocationType2, on_delete=models.CASCADE)
    variable_2 = models.ForeignKey(VariableChoices2, on_delete=models.CASCADE)
    location_2 = models.ForeignKey(Location2, on_delete=models.CASCADE)

