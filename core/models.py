from django.db import models


class Resto(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    map = models.CharField(max_length=255, blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True, help_text="Format: hh:mm - hh:mm")

    class Meta:
        managed = False
        db_table = 'resto'

    def __str__(self):
        return self.name

class RestoTag(models.Model):
    resto = models.ForeignKey(Resto, models.CASCADE)
    tag = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'resto_tag'

    def __str__(self):
        return self.tag
