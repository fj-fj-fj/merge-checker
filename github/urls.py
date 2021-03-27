from django.urls import path

from .views import IndexPageView, PullRequestDetailView

app_name = 'github'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('user-detail/', PullRequestDetailView.as_view(), name='detail'),
]
