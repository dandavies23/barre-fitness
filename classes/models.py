from django.db import models


class FitnessClass(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    instructor = models.CharField(max_length=20, null=True, blank=True)
    spaces = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
