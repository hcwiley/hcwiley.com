from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime
from tinymce.models import HTMLField

class FrontInfo(models.Model):
  about = models.TextField(blank=True, null=True, default="")

  class Meta:
    verbose_name = u'About the Front'
    verbose_name_plural = u'About the Front'

  def __unicode__(self):
    return "About Copy"

class FAQ(models.Model):
  topic = models.CharField(max_length=100, blank=False, null=False, default="")
  answer = models.TextField(blank=True, null=True, default="")

  class Meta:
    verbose_name = u'FAQ'
    verbose_name_plural = u'FAQs'

  def __unicode__(self):
    return self.topic

class Link(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  url = models.CharField(max_length=255, blank=True, null=True, default="")

  class Meta:
    ordering = ('name', )

  def __unicode__(self):
    return self.name

class FrontMedia(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  video_link = models.CharField(max_length=255, blank=True, null=True, default="")
  image = models.ImageField(upload_to='front_media/', default="", null=True, blank=True, editable=False)
  thumbnail = models.ImageField(upload_to='front_media/', default="", null=True, blank=True, editable=False)
  full_res_image = models.ImageField(upload_to='front_media/', default="", null=False, blank=False)
  is_default_image = models.BooleanField(default=False)

  def __unicode__(self):
    return self.name

  def thumb(self):
    return "%s%s" % (settings.MEDIA_URL, self.thumbnail.name)

  def img(self):
    return "%s%s" % (settings.MEDIA_URL, self.image.name)

  def full_res(self):
    return "%s%s" % (settings.MEDIA_URL, self.full_res_image.name)

  def height(self):
    try:
      return self.image.height
    except:
      return ""


  def video(self):
    html = ""
    if self.video_link.count("vimeo") > 0:
      html = '<iframe src="//player.vimeo.com/video/%s" width="600" height="300px" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>' % (self.video_link[self.video_link.rindex("/") + 1 :])
    elif self.video_link.count("you") > 0:
      if self.video_link.count("?v=") > 0:
        video = self.video_link[self.video_link.rindex("=") + 1:]
      else:
        video = self.video_link[self.video_link.rindex("/") + 1:]
      html = '<iframe width="560" height="315" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % video
    return html

  def save(self, *args, **kwargs):
    super(FrontMedia, self).save()
    self.rotateImage()
    self.saveImage()
    self.saveThumbnail()

  def rotateImage(self):
    from PIL import Image
    path = self.full_res_image.path
    image = Image.open(path)
    try:
      if self.left:
        print "turn left"
        image = image.rotate(90)
    except:
      pass
    try:
      if self.right:
        print "turn right"
        image = image.rotate(-90)
    except:
      pass
    dot = path.rindex('.')
    path = (path[:dot], path[dot:])
    path = "%s-small%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    path = path[1].strip("/")
    self.full_res_image = "%s" % (path)
    super(FrontMedia, self).save()

  def saveImage(self):
    from PIL import Image
    path = self.full_res_image.path
    image = Image.open(path)
    image.thumbnail((900,900), Image.ANTIALIAS)
    dot = path.rindex('.')
    path = (path[:dot], path[dot:])
    path = "%s-small%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    path = path[1].strip("/")
    self.image = "%s" % (path)
    super(FrontMedia, self).save()

  def saveThumbnail(self):
    from PIL import Image
    path = self.full_res_image.path
    image = Image.open(path)
    image.thumbnail((250,250), Image.ANTIALIAS)
    dot = path.rindex('.')
    path = (path[:dot], path[dot:])
    path = "%s-thumb%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_ROOT)
    path = path[1].strip("/")
    self.thumbnail = "%s" % (path)
    super(FrontMedia, self).save()

class NewsArticle(models.Model):
  name = models.CharField(max_length=255, blank=False, null=False, default="")
  text = models.TextField(blank=True, null=True, default="")
  content = HTMLField(blank=True, null=True, default='')
  date = models.DateField(default=datetime.date.today)
  is_old_news = models.BooleanField(default=False)

  class Meta:
    ordering = ['-date']
    verbose_name = u'Show Info'
    verbose_name_plural = u'Shows Info'
  
  def __unicode__(self):
    return "%s (%s)" % (self.name, self.date)

  def thumb(self):
    image = self.newsmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.newsmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/shows/%s-%s" % (self.date, self.pk)

class NewsMedia(FrontMedia):
  news_article = models.ForeignKey(NewsArticle)

class Press(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  content = HTMLField(blank=True, null=True, default='')
  date = models.DateField(default=datetime.date.today)
  is_archived = models.BooleanField(default=False)

  class Meta:
    ordering = ['-date']
    verbose_name = u'Press About the Front'
    verbose_name_plural = u'Press About the Front'
  
  def __unicode__(self):
    return "%s (%s)" % (self.name, self.date)

  def thumb(self):
    image = self.pressmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.pressmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/press/%s-%s" % (self.date, self.pk)

class PressMedia(FrontMedia):
  press_article = models.ForeignKey(Press)
class PressLink(Link):
  press_article = models.ForeignKey(Press)
