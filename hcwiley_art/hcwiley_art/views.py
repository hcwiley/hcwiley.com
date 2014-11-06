from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from artist.models import *
from media_material.models import NewsArticle, FrontInfo, FAQ

def common_args(request):
    """
    The common arguments for all gallery views.
    
    STATIC_URL: static url from settings
    """ 
    user = request.user if request.user.is_authenticated() else None
    args = {
                'STATIC_URL' : settings.STATIC_URL,
                'MEDIA_URL' : settings.MEDIA_URL,
                'user' : user,
                'PAGE_TITLE' : 'The Front',
           }
    args.update(csrf(request))
    return args

def home(req):
  args = common_args(req)
  artist = args['artist'] = Artist.objects.all()[0]
  args['medias'] = ArtistMedia.objects.filter(artist=artist)
  args['news'] = NewsArticle.objects.all()[:5]
  return render_to_response("index.jade", args)
  
def contact(req):
  args = common_args(req)
  return render_to_response("contact.jade", args)

def fundraiser(req):
  args = common_args(req)
  return render_to_response("fundraiser.jade", args)
  
def film_festival(req):
  args = common_args(req)
  return render_to_response("film_festival.jade", args)
  
def success(req):
  args = common_args(req)
  return render_to_response("success.jade", args)

def rotate(req, dirr, pk):
  if req.user.is_authenticated():
    image = ArtistMedia.objects.filter(id=pk)[0]
    if dirr == 'left':
      image.left = True
    if dirr == 'right':
      image.right = True
    image.save()
  return redirect(req.META['HTTP_REFERER'])
  
  
def about(req):
  args = common_args(req)
  args['info'] = FrontInfo.objects.all()[0]
  args['faqs'] = FAQ.objects.all()
  args['artists'] = Artist.objects.all()
  return render_to_response("about.jade", args)
  
