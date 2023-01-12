from django.db import models

# Create your models here.
class Product(models.Model):
            title = models.CharField(max_length=120) #models.Field is used to map these to database
            description =models.TextField(blank=True,null=True)
            price =models.DecimalField(decimal_places=2,max_digits=500)
            summary=models.TextField() 