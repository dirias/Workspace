# Django imports
from django.db import models
# Accessing to the django built-in user model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Creating the profile model
class Profile(models.Model):
    """
    It creates the model profile on the database, 
    using a oneToOne field to the existent Django user model
    """
    user = models.OneToOneField(User,on_delete=CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/picture', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.usernam
    