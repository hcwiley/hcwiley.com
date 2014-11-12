from artist.models import *
from django.contrib import admin
from django_admin_bootstrapped.admin.models import SortableInline


class ParentMediaAdmin(admin.ModelAdmin):
  model = ParentMedia
  readonly_fields = ['admin_thumb']

class ArtistMediaInlineSort(admin.StackedInline, SortableInline):
  model = ArtistMedia
  fields = ['position']
  extra = 0

class ArtistMediaInline(admin.TabularInline):
  model = ArtistMedia
  exclude = ['position']
  fields = ['name', 'video_link', 'admin_thumb', 'full_res_image',
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
  model = Artist

class ArtistMediaCategoryAdmin(admin.ModelAdmin):
  model = ArtistMediaCategory
  inlines = [
    ArtistMediaInlineSort,
  ]
  inlines = [
    ArtistMediaInline,
    ArtistMediaInlineSort,
  ]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(ParentMedia, ParentMediaAdmin)
admin.site.register(ArtistMedia, ArtistMediaAdmin)
admin.site.register(ArtistMediaCategory, ArtistMediaCategoryAdmin)

admin.site.register(Press)
