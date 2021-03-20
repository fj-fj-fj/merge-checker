from django.urls import path

from .views import index, get_details

app_name = 'github'

urlpatterns = [
    path('', index, name='index'),
    path('user-detail/', get_details, name='detail'),
]
