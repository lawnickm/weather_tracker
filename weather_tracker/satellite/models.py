from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

# Create your models here.

class Satellite(models.Model):
    # Satellite Image infomation
    SATALLITE_TYPE_CHOICES = [
        ('15', 'NOAA 15'),
        ('18', 'NOAA 18'),
        ('19', 'NOAA 19'),
    ]
    # image = models.URLField(max_length=500) # Image by URL
    image = models.ImageField(blank=False, null=False,
                              upload_to='satellite/')  # Image by uploading
    satelliteID = models.CharField(
        max_length=2,
        choices=SATALLITE_TYPE_CHOICES,
        default='15',
        blank=False,
        null=False,
    )

    # Image time stamp.
    # auto_now_add=True: takes the instant datetime when a satellite obj is created
    timeStamp = models.DateTimeField(auto_now_add=True)

    # Creates image path. As: localhost:8000/[image_url]
    def get_image(self):
        if self.image:
            return "https://weather-tracker-pdwt-main-pgmcdrxw5a-wm.a.run.app" + self.image.url
        else:
            return ""

    # Define display name of an object in the Django admin site.
    def __str__(self):
        return f'{self.get_satelliteID_display()} ({self.timeStamp})'
