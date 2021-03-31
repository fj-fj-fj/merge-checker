# Merge-Checker

[English version](README.eng.md)


[![Python](https://img.shields.io/static/v1?label=Python&style=plastic&logofor-the-badge&message=3&color=3776AB&logo=PYTHON)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-django-green?style=flat&logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![CI](https://github.com/fj-fj-fj/merge-checker/actions/workflows/test.yml/badge.svg)](https://github.com/fj-fj-fj/merge-checker/actions/workflows/test.yml)

## Что такое и зачем 
Веб-сервис, который позволит узнать, в какие проекты конкретный пользователь Гитхаба делал пул-реквесты и их смерджили. 

- На главной странице введите ник пользователя на Гитхабе и нажмите `Send`
- В результате отобразится страница со списком проектов, в которые пользователь делал пул-реквест и его смерджили. По каждому проекту видно:
  - название проекта
  - линк на проект на Гитхабе
  - количество звёзд на Гитхабе
  - линки на смерженные пул-реквесты от пользователя
  - линки на несмерженные пул-реквесты от пользователя
  - у каждого пул-реквеста отображается количество комментариев в этом пул-реквесте

Веб-сервис общаeтся с Гитхабом через АПИ.

#
Поскольку для неаутентифицированных запросов ограничение скорости позволяет обрабатывать до [60 запросов в час](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting "Ограничение скорости"), желательно добавить токен авторизации в `app.core.settings.base.TOKEN`. В модуле `api.py` приложения `github` есть опциональный `import` для токена.

#
## Установка и запуск
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