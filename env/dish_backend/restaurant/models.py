from django.db import models

# Create your models here.
class Restaurant(models.Model):
    external_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    image_url = models.URLField(null=True)
    menu_url = models.URLField(null=True)
    category = models.JSONField(default=list, null=True) 
    review_count = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    def __str__(self):
        return self.name