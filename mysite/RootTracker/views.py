from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import webbrowser, os.path

def index(request):
        purpose = "Program Interface to be Implemented here."
        template = loader.get_template('RootTracker/index.html')
        context = {
            'purpose': purpose,
        }
        return HttpResponse(template.render(context, request))
    

