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

class User(models.Model):
    id = models.AutoField(primary_key=True)
    externalId = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Ensure to handle password securely - using auth library
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    reviews_left = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    external = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    restaurant_external_id = models.CharField(max_length=50)
    food_item_cat = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating_ovr = models.DecimalField(max_digits=2, decimal_places=1)
    grade_rating_ovr = models.IntegerField()
    rating_cat = models.DecimalField(max_digits=2, decimal_places=1)
    grade_rating_cat = models.IntegerField()
    reviews = models.IntegerField()

    def __str__(self):
        return self.name

class ReviewTable(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255, unique=True)
    date = models.DateField()
    user_external_id = models.CharField(max_length=255)
    menu_external_id = models.CharField(max_length=255)
    review_text = models.TextField()
    review_rating_ovr = models.DecimalField(max_digits=2, decimal_places=1)
    review_scale_ovr = models.IntegerField()
    review_rating_cat = models.DecimalField(max_digits=2, decimal_places=1)
    review_scale_cat = models.IntegerField()

    def __str__(self):
        return self.external_id