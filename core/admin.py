from django.contrib import admin
from .models import GalleryImage, ContactMessage, ContactInfo, Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'album', 'uploaded_at')
    list_filter = ('album',)
    search_fields = ('caption',)

admin.site.register(ContactMessage)
admin.site.register(ContactInfo)

    

