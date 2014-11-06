from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from front_material.models import Link, PressLink
from the_front.views import common_args

def home(req):
  args = common_args(req)
  args['links'] = Link.objects.exclude(id__in=PressLink.objects.all())
  return render_to_response("links.jade", args)

