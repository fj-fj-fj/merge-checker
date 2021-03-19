from django.urls import path

from .views import index, user_details

app_name = 'github'

urlpatterns = [
    path('', index, name='index'),
    path('user-detail/', user_details, name='detail'),
]
