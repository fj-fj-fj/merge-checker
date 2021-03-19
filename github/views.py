from django.shortcuts import render


def index(requests):
    context = {}
    return render(requests, 'github/index.html', context)

def user_details(requests):
    context = {}
    return render(requests, 'github/project_list.html', context)
