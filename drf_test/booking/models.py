from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    datetime1 = models.DateTimeField(null=True, blank=True)
    datetime2 = models.DateTimeField(null=True, blank=True)
