from typing import Dict, Any

from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render

from .api import show_project_list_with_pull_requests


class IndexPageView(TemplateView):

    template_name: str = 'github/index.html'


class PullRequestDetailView(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        projects: Dict[str, Any] = show_project_list_with_pull_requests(request)
        context: Dict[str, Any] = {
            'user': projects['owner'],
            'projects': projects['projects'],
        }
        return render(request, 'github/project_list.html', context)
