from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {
        'template_var': 'This is the simpleApp index.'
    }
    return HttpResponse(template.render(context, request))

def hi(request):
    template = loader.get_template('greet.html')
    context = {}
    return HttpResponse(template.render(context, request))

def greet(request, someone):
    template = loader.get_template('greet.html')
    context = { 'greet_someone': someone}
    return HttpResponse(template.render(context, request))