from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from users.models import Profile

def default_expiry_date():
    return now().date() + timedelta(days=365)


class Passport(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='passport')
    passport_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField(default=now)
    expiry_date = models.DateField(default=default_expiry_date)

    MEMBERSHIP_TIERS = [
        ('BASIC', 'Basic'),
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('PLATINUM', 'Platinum'),
    ]
    membership_tier = models.CharField(max_length=10, choices=MEMBERSHIP_TIERS, default='BASIC')
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.passport_number} - {self.profile.user.username}"

    def is_valid(self):
        return now().date() <= self.expiry_date
