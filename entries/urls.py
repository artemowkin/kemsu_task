from django.urls import path

from .views import CreateEntryView, all_entries


urlpatterns = [
    path('create/', CreateEntryView.as_view(), name='create_entry'),
    path('all/', all_entries, name="all_entries"),
]
