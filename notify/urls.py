from django.urls import path
from .views import (NotificationsList, NotificationDetailed, NotificationCreate, NotificationDelete, get_profile_page,
                    response_to_notification_accept, response_to_notification_reject)

urlpatterns = [
    path("notifications/", NotificationsList.as_view(), name="notifications_list"),
    path("notifications/<int:pk>", NotificationDetailed.as_view(), name="notification"),
    path("notifications/create", NotificationCreate.as_view(), name="notification_create"),
    path("notifications/<int:pk>/delete", NotificationDelete.as_view(), name="notification_delete"),
    path("notifications/personal_page", get_profile_page, name="personal_page"),
    path("notifications/accept/<int:pk>", response_to_notification_accept, name="accept_btn"),
    path("notifications/reject/<int:pk>", response_to_notification_reject, name="delete_btn"),
]
