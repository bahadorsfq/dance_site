from django.contrib import admin
from .models import GalleryImage
from .models import ContactMessage, ContactInfo

admin.site.register(ContactMessage)
admin.site.register(ContactInfo)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)

