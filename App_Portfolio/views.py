from django.http import response
from django.shortcuts import get_object_or_404, render
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext, context

import requests

from api.models import Project

# Create your views here.


def home(request):
    return render(request, 'project/home.html',)


def list(request):
    response = requests.get(
        'https://akash-portfolio-21.herokuapp.com/api/project-list/')
    data = response.json()
    context = {
        'data': data,
    }

    return render(request, 'project/list.html', context)


def project_detail(request, pk):
    # project = Project.objects.get(pk=pk)
    project = get_object_or_404(Project, pk=pk)
    # print(project[0].title)
    # response = requests.get('http://127.0.0.1:8000/api/project-detail/pk/')
    # project = response
    # print(project.image)
    # print(project.description)

    context = {
        'project': project,
    }

    return render(request, 'project/project_detail.html', context)



def contact(request):
    success_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
    
        send_mail(subject, message, from_email, ['akashdemo1234@gmail.com'], fail_silently=False)
        context = {
            'name' : name,
            'success_msg' : "successfully send your email",
        }
        return render(request, 'project/contact.html', context)
    else:
        return render(request, 'project/contact.html', context = { 'success_msg' : success_msg})

        

    
    