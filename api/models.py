from django.db import models

# Create your models here.
class Locations(models.Model):
    location = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.location

class Items(models.Model):
    item = models.CharField(max_length=25)
    itemDetail = models.TextField(default=None, null=True)
    itemLocation = models.ForeignKey(Locations,on_delete=models.CASCADE)

