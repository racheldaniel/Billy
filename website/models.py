from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """Defines the Profile table model-- a one-to-one with the Django User model

        Returns: __str__ user and state

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"User: {self.user} State:{self.state}"

# # Methods define signals so that Profile model will automatically be created whenever a user is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class UserBill(models.Model):
    """Defines the UserBill table model for a User with saved proPublica bill id

        Returns: __str__ user, pp_bill_id and comment

    """
    # cascade used here because open orders are hard deleted, so we want to remove join tables also
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pp_bill_id = models.CharField(max_length=100, blank=False)
    comment = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"User: {self.user} Bill Id:{self.pp_bill_id} Comment:{self.comment}"
