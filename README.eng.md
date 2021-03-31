# Merge-Checker

[Russian version](README.md)


[![Python](https://img.shields.io/static/v1?label=Python&style=plastic&logofor-the-badge&message=3&color=3776AB&logo=PYTHON)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-django-green?style=flat&logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![CI](https://github.com/fj-fj-fj/merge-checker/actions/workflows/test.yml/badge.svg)](https://github.com/fj-fj-fj/merge-checker/actions/workflows/test.yml)

## Introduction
 See which projects the GitHub user made pull-requests to that were merged.

- On the main page, enter the username on the GitHub and click `Send`
- As a result, a page with a list of projects to which the user made a pull-request to that was merged. For each project you can see:
  - the name of the project
  - link to the project on GitHub
  - number of stars on GitHub
  - links to merged pull-requests from the user
  - links to non-merciless pull-requests from the user
  - each pull-request displays the number of comments in this pull-request
 
The WEB-service is used by Githab API.

#
Since for unauthenticated requests, rate limiting allows up to [60 requests per hour](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting "Rate limiting") , it is advisable to add an authorization token to `app.core.settings.base.TOKEN`. The `api.py` module of the` github` application has an optional `import` for the token.

#
## Installation
```bash
git clone https://github.com/fj-fj-fj/merge-checker.git
cd merge-checker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

## Docker
```bash
git clone https://github.com/fj-fj-fj/merge-checker.git
cd merge-checker
docker build . --tag <image_name>
docker run --port 8000:8000 <image_name>
```