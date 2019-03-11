from django.db import models

class VariableType(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name