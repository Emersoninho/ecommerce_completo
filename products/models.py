from django.db import models

class ProductMenager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=100.00)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    objects = ProductMenager()
    
    def __str__(self):
        return self.title