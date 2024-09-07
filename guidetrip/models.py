from django.db import models

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
    class Meta:
        verbose_name_plural = 'Trips'

    rec_owner = models.CharField(max_length=100, null=True, blank=True)
    categories = models.ForeignKey('categories', null=True, blank=True, on_delete=models.SET_NULL)
    venue = models.CharField(max_length=254)
    description = models.TextField()
    day = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    spaces = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    Cost = models.DecimalField(max_digits=6, decimal_places=2)
    dates = models.DateField(verbose_name="Date of Event", blank=True) 
    location = models.CharField(max_length=254)
    locale = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_rec_owner(self):
        return self.rec_owner

    def __str__(self):
        return self.venue