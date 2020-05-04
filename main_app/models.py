from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # favorite_color = models.CharField(max_length=50)
    # can add other attridbutes to check our users. 