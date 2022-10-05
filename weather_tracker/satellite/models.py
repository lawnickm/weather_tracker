from django.db import models

# Create your models here.

class Satellite(models.Model):
    # Satellite Image infomation
    IMAGE_TYPE_COHICES = [
        ('1', 'Type 1'),
        ('2', 'Type 2'),
        ('3', 'Type 3'),
    ]
    image = models.ImageField()
    imageType = models.CharField(
        max_length=1,
        choices=IMAGE_TYPE_COHICES,
        default='1',
    )

    # Location stored as string
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)

    # Location stored as coordinates
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)

    # Image time stamp.
    timeStamp = models.DateTimeField()
