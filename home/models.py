from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.EmailField(max_length=122)
    name=models.CharField(max_length=112)
    country=models.CharField(max_length=112)
    massage=models.CharField(max_length=500)
    

    def __str__(self):
        return self.name
