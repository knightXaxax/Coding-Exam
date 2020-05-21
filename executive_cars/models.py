from django.db import models


class ExecutiveCarsInformation(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'executive_cars_information'
