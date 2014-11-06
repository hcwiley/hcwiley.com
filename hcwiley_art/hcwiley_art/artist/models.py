from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from media_material.models import FrontMedia

# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  slug = models.CharField(max_length=100, blank=True, null=True, default="", editable=False)
  bio = models.TextField(blank=True, null=True, default="")
  artist_statement = models.TextField(blank=True, null=True, default="")
  user = models.ForeignKey(User)
  website = models.CharField(max_length=100, blank=True, null=True, default="")
  email = models.CharField(max_length=100, blank=True, null=True, default="")
  cv = models.FileField(upload_to='front_media/', blank=True, null=True, default="")

  class Meta:
    ordering = ['name']
  
  def __unicode__(self):
    return self.name

  def save(self):
    super(Artist, self).save()
    self.slug = slugify(self.name)
    super(Artist, self).save()

  def cv_link(self):
    return "%s%s" % (settings.MEDIA_URL, self.cv.name)

  def cv_name(self):
    if self.cv:
      return "%s-CV%s" % (self.name, self.cv.name[self.cv.name.rindex("."):])
    else:
      return ""

  def web(self):
    if self.website.count("http") > 0:
      return self.website
    else:
      return "http://%s" % self.website

  def thumb(self):
    image = self.artistmedia_set.filter(is_default_image=True)
    if len(image) == 0 :
      image = self.artistmedia_set.all()
    if len(image) == 0 :
      return ""
    image = image[0]
    return image.thumb()

  def get_absolute_url(self):
    return "/artists/%s" % (self.slug)

class ArtistMedia(FrontMedia):
  artist = models.ForeignKey(Artist)
  position = models.PositiveSmallIntegerField("Position", default=1)
  dimensions = models.CharField(max_length=100, blank=True, null=True, default="")
  medium = models.CharField(max_length=100, blank=True, null=True, default="")
  year = models.CharField(max_length=4, blank=True, null=True, default="")
  class Meta:
    ordering = ('position', )

  def admin_thumb(self):
    html = ''
    if self.thumbnail:
      html += "<div class='col-xs-12'><div class='col-xs-6'><a class='btn btn-block btn-sm btn-success' href='/image/rotate/left/%s'>rotate left</a></div>"% (self.id)
      html += "<div class='col-xs-6'><a class='btn btn-block btn-sm btn-danger' href='/image/rotate/right/%s'>rotate right</a></div></div>"% (self.id)
      html += "<img src='%s'/>" % ( self.thumb())
      return html
    return ""
  admin_thumb.allow_tags = True

