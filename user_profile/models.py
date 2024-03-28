from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='user_profile/images/')
    mobile_no = models.CharField(max_length = 12)
    age = models.IntegerField(default=18)
    portfolio = models.URLField(blank=True)
    sex = models.CharField(choices = SEX_CHOICES, max_length = 10, default="Male")
    bio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)

    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
    # Sync first_name field with user.first_name
        # if not self.first_name:
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        self.email = self.user.email
        super().save(*args, **kwargs)