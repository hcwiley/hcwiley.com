from artist.models import *
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline

class ArtistMediaInlineSort(admin.StackedInline, SortableInline):
  model = ArtistMedia
  fields = ['position']
  extra = 0

class ArtistMediaInline(admin.TabularInline):
  model = ArtistMedia
  exclude = ['position']
  fields = ['name', 'video_link', 'full_res_image', 'admin_thumb',
      'is_default_image', 'dimensions', 'medium', 'year']
  readonly_fields = ['admin_thumb']

def generate_thumbnails(modeladmin, request, queryset):
  for obj in queryset:
    obj.saveThumbnail()
    obj.saveImage()
generate_thumbnails.short_description = "Re-generate thumbnail images"

class ArtistMediaAdmin(admin.ModelAdmin):
  actions = [generate_thumbnails]

class ArtistAdmin(admin.ModelAdmin):
  inlines = [
    ArtistMediaInline,
    ArtistMediaInlineSort,
  ]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtistMedia, ArtistMediaAdmin)
