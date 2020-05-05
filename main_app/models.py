from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # favorite_color = models.CharField(max_length=50)
    # can add other attridbutes to check our users. 

class Comment(models.Model):
    text = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    # we may not even need this since we don't even use the "view a toy" page like a "view a comment" page
 
    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.id})

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    comments = models.ManyToManyField(Comment)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})