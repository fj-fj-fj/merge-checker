from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render

from .api import get_project_user_list_with_pull_requests


class IndexPageView(TemplateView):

    template_name = 'github/index.html'


class PullRequestDetailView(View):

    def post(self, requests):
        projects = get_project_user_list_with_pull_requests(requests)
        context = {
            'user': projects['owner'],
            'projects': projects['projects'],
        }
        return render(requests, 'github/project_list.html', context)
