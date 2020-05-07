from django.db import models


class Catalog(models.Model):
    phone = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    room = models.CharField(max_length=50, null=True, blank=True)
    floor = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self): return '%s - %s' % (self.id, self.name)
