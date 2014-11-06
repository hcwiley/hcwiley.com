from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from front_material.models import Press, PressMedia
from the_front.views import common_args

def home(req):
  args = common_args(req)
  args['press'] = Press.objects.filter(is_archived=False)
  return render_to_response("press/list.jade", args)

def press(req, pk):
  args = common_args(req)
  press = Press.objects.get(pk=pk)
  if not press:
    args['error'] = 'No press found'
    return render_to_response("error.jade", args)
  args['press'] = press
  args['press_images'] = PressMedia.objects.filter(press_article=press)
  return render_to_response("press/show.jade", args)
