from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone

# to create the one field for offer shown in the title bar

class TitleOffer(models.Model):
    date = models.DateTimeField(default=timezone.now)
    offer = models.TextField(max_length=200 , help_text='This will shown in title bar offer')


# The advertiment image add in 

class Advertise(models.Model):
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to = 'ad_img')
    dis = models.TextField( blank=True )

# The blog section for the home page 

class Blog (models.Model):
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    img = models.ImageField( upload_to = 'blog_img')
    dis = TextField()



