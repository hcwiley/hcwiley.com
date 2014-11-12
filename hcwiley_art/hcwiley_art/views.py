from django.shortcuts import render_to_response, redirect
#from django.http import Http404
from django.conf import settings
from django.core.context_processors import csrf
from artist.models import *

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
    artist = args['artist'] = Artist.objects.all()[0]
    categories = args['categories'] = ArtistMediaCategory.objects.all()
    args['medias'] = {}
    for category in categories:
      args['medias'][category.name] = ArtistMedia.objects.filter(category=category)[:3]
    args.update(csrf(request))
    return args

def home(req):
  args = common_args(req)
  return render_to_response("index.jade", args)
  
def contact(req):
  args = common_args(req)
  return render_to_response("contact.jade", args)

def success(req):
  args = common_args(req)
  return render_to_response("success.jade", args)

def rotate(req, dirr, pk):
  if req.user.is_authenticated():
    image = ParentMedia.objects.filter(id=pk)[0]
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
  
