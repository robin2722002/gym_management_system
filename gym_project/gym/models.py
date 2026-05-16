from django.db import models
from django.conf import settings

class TrainerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
    upload_to='trainer_photos/',
    null=True,
    blank=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.user.name
    

from django.db import models
from accounts.models import User

class Booking(models.Model):

    member = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="member_booking"
    )

    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trainer_booking"
    )

    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.username} → {self.trainer.username}"