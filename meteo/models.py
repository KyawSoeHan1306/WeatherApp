from django.db import models

class Worldcities(models.Model):
    city = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lng = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    id = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'worldcities'