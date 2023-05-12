from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from .categories import CHOICES_FOR_CATEGORY


class Notification(models.Model):
    title = models.CharField(unique=True, blank=False, max_length=128)
    description = RichTextUploadingField(blank=True, null=True)
    category = models.CharField(blank=False, choices=CHOICES_FOR_CATEGORY, max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/notifications/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Response(models.Model):
    text = models.TextField(blank=False)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    responded_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.responded_user.username
