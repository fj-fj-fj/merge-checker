import requests

from typing import List, Dict, Any, Optional
from core.settings.base import API_URL

try:
    from core.settings.local import GITHUB_TOKEN as __T

    URL = API_URL + f'&authorization_request={__T}'
except ImportError:
    pass


def get_merge_info(user: str) -> Dict[str, Any]:
    user_url: str = URL.format(user)
    pull_requests: list = _get_pull_requests(user_url)
    if pull_requests:
        projects: list = _get_project_list(pull_requests)
        return {'projects': projects}
    return {'projects': None}


def _get_pull_requests(user: str) -> Optional[List[dict]]:
    """Get and return pull-requests user list."""
    pull_requests: list = _get_json_data(user).get('items')

    if pull_requests is None:
        return []

    for pull in pull_requests:
        pull_request_url: str = pull.get('pull_request').get('url')
        pull_request_info: dict = _get_json_data(pull_request_url)

        pull['merged'] = pull_request_info.get('merged')
        pull['html_url'] = pull_request_info.get('html_url')

    return pull_requests


def _get_project_list(pulls: list) -> List[dict]:
    """Create and return project list."""
    projects = []
    names = set()

    for pull in pulls:
        repo_url: str = pull.get('repository_url')
        repo: dict = _get_json_data(repo_url)

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


def _get_json_data(url: str) -> Dict[str, Any]:
    return requests.get(url).json()
