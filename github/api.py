import requests
from typing import List, Dict, Any, Optional

from core.settings.base import API_URL
from django.http import HttpRequest

try:
    from core.settings.local import GITHUB_TOKEN as __T

    URL: str = API_URL + f'&authorization_request={__T}'
except ImportError:
    pass


def show_project_list_with_pull_requests(request: HttpRequest) -> Dict[str, Any]:
    username: str = request.POST.get('search').strip()
    projects: dict = _generate_project_list_with_pull_requests(username)
    projects: Optional[list] = projects.get('projects')

    return {
        'owner': username,
        'projects': projects if projects is not None else []
    }


def _generate_project_list_with_pull_requests(user: str) -> Dict[str, Any]:
    user_url: str = URL.format(user)
    pull_requests: list = _generate_pull_request_list(user_url)
    if pull_requests:
        projects: list = _generate_project_list(pull_requests)
        return {'projects': projects}
    return {'projects': None}


def _generate_pull_request_list(user: str) -> Optional[List[dict]]:
    pull_requests: list = _fetch_data_from_github_API(user).get('items')

    if pull_requests is None:
        return []

    for pull in pull_requests:
        pull_request_url: str = pull.get('pull_request').get('url')
        pull_request_info: dict = _fetch_data_from_github_API(pull_request_url)

        pull['merged'] = pull_request_info.get('merged')
        pull['html_url'] = pull_request_info.get('html_url')

    return pull_requests


def _generate_project_list(pulls: list) -> List[dict]:
    projects: list = []
    names = set()

    for pull in pulls:
        repo_url: str = pull.get('repository_url')
        repo: dict = _fetch_data_from_github_API(repo_url)

        if (name := repo.get('name')) not in names:
            names.add(name)
            projects.append({
                'name': name,
                'html_url': repo.get('html_url'),
                'stars': repo.get('stargazers_count'),
                'pulls': [pull]})
        elif name in names:
            for project in projects:
                if project['name'] == name:
                    project['pulls'].append(pull)

    return projects


def _fetch_data_from_github_API(url: str) -> Dict[str, Any]:
    return requests.get(url).json()
