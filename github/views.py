from typing import Optional

from django.shortcuts import render

from .api import get_pull_request_data


def index(requests):
    return render(requests, 'github/index.html')


def get_details(requests):
    username: str = requests.POST.get('search').strip()
    projects: dict = get_pull_request_data(username)

    projects: Optional[list] = projects.get('projects')

    if projects is None:
        return render(requests, 'github/index.html')

    context = {
        'projects': projects,
        'user': username,
    }
    return render(requests, 'github/project_list.html', context)
