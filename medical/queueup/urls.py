from django.urls import path

from medical.queueup.views import lineup_view, cancel_lineup_view

app_name = "queueup"
urlpatterns = [
    path("lineup/", view=lineup_view, name="lineup"),
    path("cancel-lineup/", view=cancel_lineup_view, name="cancel_lineup"),
]
