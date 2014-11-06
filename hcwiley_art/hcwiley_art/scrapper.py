from pyquery import PyQuery
import urllib, cStringIO
from front_material.models import *
from datetime import datetime
from django.core.files.images import ImageFile
from django.conf import settings
from PIL import Image
from PIL import ImageFile as IFile
IFile.MAXBLOCK = 2**20

def main():
  base = "http://www.nolafront.org/pages/"
  
  req = urllib.urlopen('%sarchive.htm' % base)
  html = req.read()
  pq = PyQuery(html)
  
  ass = pq("a.style2")
  
  a_iter = ass.items()
  a = a_iter.next()
  count = 0
  last_year = "2013"
  while count < len(ass) - 1:
    href = "%s%s" % ( base, a.attr('href') )
    name = a.text()
    if len(name) > 100:
      name = name[:14]
    artists_info = a.parent().text()
    artists_info = artists_info[len(name)+1:]
    print href
    nq = PyQuery(urllib.urlopen(href).read())
    imgs = nq.find('img')
    n_iter = imgs.items()
    img = n_iter.next()
    text = ""
    i = 0
    news, created = NewsArticle.objects.get_or_create(name=name)
    news.save()
    while i < len(imgs) - 1:
      i += 1
      img_orig = n_iter.next()
      src = "%s%s" % (base, img_orig.attr('src'))
      img_name = "%s-%d.jpg" % (name, i)
      if  len(NewsMedia.objects.filter(news_article=news,name=img_name)) > 0:
        continue
      try:
        img = cStringIO.StringIO(urllib.urlopen(src).read())
        img = Image.open(img)
        img_path = "%s/front_media/%s" % (settings.MEDIA_ROOT, img_name)
        portrait = float(img.size[0] / img.size[1]) < 1.0
        img.save(img_path, "JPEG", quality=90, optimize=True)
        img = ImageFile(open(img_path))
        media, created = NewsMedia.objects.get_or_create(news_article=news, full_res_image=img, portrait=portrait, name=img_name)
        img_orig.attr('src', "%s%s" % (settings.MEDIA_URL, media.full_res_image.name))
        img.close()
      except:
        print "error on saving: %s" % src
    html = nq.find("body").html()
    if href.find("archive-december 13") >= 0:
      print html
    is_content = False
    lines = html.split("\n")
    news.text = ""
    for line in lines:
      if line.find("LINKS") >= 0:
        is_content = True
        continue
      if is_content:
        if line.find("</body>") >= 0:
          is_content = False
          continue
        news.text += line
    news.name = name
    news.is_old_news = True
    news.artists_info = artists_info
    news.name = name
    date = name.split('-')
    date = date[0]
    if date.endswith(" "):
      date = date.rstrip(" ")
    try:
      date.index(',') 
    except:
      try:
        date = "%s, %s" % (date, name.split(", ")[1])
      except:
        pass
    try:
      date = datetime.strptime(date, "%B %d, %Y")
      last_year = "%d" % date.year
    except:
      print 'didnt get a date 1'
      print date
      try:
        date = "%s, %s" % (date, last_year)
        date = datetime.strptime(date, "%B %d, %Y")
        last_year = "%d" % date.year
      except:
        print 'didnt get a date 2'
        date = datetime.strptime(last_year, "%Y")
    news.date = date
    news.save()
    count += 1
    a = a_iter.next()
  
  #href = archive[0]['href']
  #name = archive[0]['name']
  #text = archive[0]['text']
  #print text
  
  '''
  lines = req.readlines()
  ass = []
  for line in lines:
    try:
      line.index('<a')
      ass.append(line)
    except:
      continue
  
  links = []
  ass.pop(0)
  for a in ass:
    start = a.index('href="')
    end = a.index('.htm"')
    links.append("%s%s" % (base, a[start:end]))
  '''
