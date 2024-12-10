from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Additional fields for the passport user details
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # Address fields (optional)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)

    # Profile picture (optional)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
