from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from artist.models import *
from the_front.views import common_args

def home(req):
  args = common_args(req)
  args['artists'] = Artist.objects.all()
  args['artists_images'] = ArtistMedia.objects.all()
  return render_to_response("artist/list.jade", args)

def artist(req, slug):
  args = common_args(req)
  artist = Artist.objects.filter(slug=slug)
  if len(artist) == 0:
    args['error'] = 'No artist found'
    return render_to_response("error.jade", args)
  artist = artist[0]
  args['artist'] = artist
  args['artist_media'] = ArtistMedia.objects.filter(artist=artist)
  return render_to_response("artist/show.jade", args)

