from django.shortcuts import render
from django.conf import settings
# Create your views here.


def main(request):
    template_name = 'main/main.html'
    context = {'developer_github_url': settings.DEVELOPER_GITHUB_URL,
               'project_github_url': settings.PROJECT_GITHUB_URL}

    return render(request, template_name, context)