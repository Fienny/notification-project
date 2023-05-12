from django.contrib import admin

from django import forms
from django.contrib import admin
# from ckeditor.widgets import CKEditorUploadingWidget

from .models import Notification, Response


# class PostAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Notification
#         fields = '__all__'
#
#
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm


admin.site.register(Notification)

admin.site.register(Response)

