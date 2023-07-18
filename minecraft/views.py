from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from minecraft.actions.index import get_context_index
    

def index(request):
    template = loader.get_template("server_manager/index.html")
    context = get_context_index()
    return HttpResponse(template.render(context, request))


def server_list(request):
    template = loader.get_template("server_manager/server_list.html")
    context = get_context_index()
    return HttpResponse(template.render(context, request))


def server(request):
    template = loader.get_template("server_manager/server.html")
    context = get_context_index()
    return HttpResponse(template.render(context, request))
