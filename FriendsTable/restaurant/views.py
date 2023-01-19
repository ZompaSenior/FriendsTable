"""Restaurants views"""

# Std Import
# from datetime import datetime

# Site-package
from django.http.response import HttpResponse
# from django.http.response import HttpResponseRedirect
from django.template import loader
# from django.urls.base import reverse

# App import
from . import models as m

def landing_page(request):
    """Represents the page at witch users arrive first."""
    
    main_object_list = m.Restaurant.objects.filter(trash_state = 0)
    
    template = loader.get_template('landing_page.html')

    context = {
        'main_object_list': main_object_list
        }
    
    return HttpResponse(template.render(context, request))
