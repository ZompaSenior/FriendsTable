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
from restaurant import models as rm

def tables(request, master_id):
    """Represents the page at witch users arrive first."""
    
    master_object = rm.Restaurant.objects.filter(id = master_id).first()
    main_object_list = m.Table.objects.filter(
        trash_state = 0).filter(restaurant_id = master_id)
    
    template = loader.get_template('tables.html')

    context = {
        'master_object': master_object,
        'main_object_list': main_object_list
        }
    
    return HttpResponse(template.render(context, request))
