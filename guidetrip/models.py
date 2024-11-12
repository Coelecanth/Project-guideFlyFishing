from django.db import models
from django.contrib.auth.models import User

class categories(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class trips(models.Model):
    class Meta:3
    verbose_name_plural = 'Trips'

    rec_owner = models.CharField(max_length=100, null=True, blank=True)
    categories = models.ForeignKey('categories', null=True, blank=True, on_delete=models.SET_NULL)
    venue = models.CharField(max_length=254)
    description = models.TextField()
    day = models.DecimalField(verbose_name="Days duration", max_digits=2, decimal_places=0, null=True, blank=True)
    spaces = models.DecimalField(verbose_name="Spaces Avialable", max_digits=2, decimal_places=0, null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    dates = models.DateField(verbose_name="Date of Event", null=True, blank=True) 
    location = models.CharField(verbose_name="Country location", max_length=254)
    locale = models.CharField(verbose_name="County/Region location", max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_rec_owner(self):
        return self.rec_owner

    def __str__(self):
        return self.venue