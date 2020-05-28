from django.urls import path

from medical.queueup.views import lineup_view, cancel_lineup_view, get_queue_list_view, index_view

app_name = "queueup"
urlpatterns = [
    path("lineup/", view=lineup_view, name="lineup"),
    path("cancel-lineup/", view=cancel_lineup_view, name="cancel_lineup"),
    path("list/", view=get_queue_list_view, name="list"),

    path("", view=index_view, name='index')
]
