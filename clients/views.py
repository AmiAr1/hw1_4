from django.shortcuts import render, HttpResponse
from .models import Client



def contacts(request):
    response = HttpResponse('<h1>тел: 0702818199<h1>')
    return response


def about(request):
    return render(request, 'about.html')


def name_list(request):
    context = {}
    clients_list = Client.objects.all()
    context['clients_list'] = clients_list
    html_page = render(request, 'name.html', context)
    return html_page