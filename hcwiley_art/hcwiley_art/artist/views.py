from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from artist.models import *
from hcwiley_art.views import common_args

def home(req):
  args = common_args(req)
  args['artists'] = Artist.objects.all()
  args['artists_images'] = ArtistMedia.objects.all()
  return render_to_response("artist/list.jade", args)

def category(req, slug):
  args = common_args(req)
  category = ArtistMediaCategory.objects.filter(slug=slug)
  if len(category) == 0:
    args['error'] = 'No category found'
    return render_to_response("error.jade", args)
  args['category_media'] = ArtistMedia.objects.filter(category=category)
  return render_to_response("artist/show.jade", args)

