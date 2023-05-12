from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError
from django_filters import ModelMultipleChoiceFilter

from .models import Notification, Response


class NotificationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    # category = ModelMultipleChoiceFilter(
    #     field_name="post_category",
    #     queryset=Category.objects.all(),
    #     label="Category",
    # )

    class Meta:
        model = Notification
        fields = [
            'title',
            'description',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("description")

        heading = cleaned_data.get('title')
        if heading == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class ResponseSend(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('text', 'notification', 'responded_user')
        widgets = {
            'notification': forms.HiddenInput(),
            'responded_user': forms.HiddenInput(),
        }
