from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email Address')
    whatsapp_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="WhatsApp number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        verbose_name='WhatsApp Number',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'whatsapp_number']

    def __str__(self):
        return self.email


class Profile(models.Model):
    # Link to the built-in User model
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    # Profile picture (optional)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
