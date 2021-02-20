from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    category=models.CharField(max_length=20,blank=False,null=False)
    image=models.ImageField(null=True, blank=True, upload_to="blog/images/")

    def __str__(self):
        return self.title + " by " + self.author
        
