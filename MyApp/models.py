from django.db import models
import uuid as uuid

# Create your models here.
class Product(models.Model):
    UserID = models.CharField(max_length=300, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=2000)
    price = models.IntegerField()
    brand = models.CharField(max_length=122)
    item = models.CharField(max_length=122)
    
    # def __str__(self):
    #     return self.title
