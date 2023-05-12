from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.shortcuts import redirect

from .models import Response


@receiver(post_save, sender=Response)
def response_created_mail(sender, instance, **kwargs):
    user_email = instance.responded_user.email
    if user_email != "":
        send_mail(
            subject=f"{instance.responded_user.username}",
            message="Your response has been created successfully!",
            from_email="imfyashya@yandex.ru",
            recipient_list=[f"{user_email}"]
        )
