from django.db import models


class Photo(models.Model):

    captions = models.CharField(max_length=80)
    photos = models.ImageField(upload_to="sensor_photos")

    def __str__(self):
        return self.captions
