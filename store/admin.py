from django.contrib import admin
from .models import Package
from .models import OrientalMusic

admin.site.register(OrientalMusic)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    fields = ('title', 'description', 'price', 'cover_image', 'video_file', 'is_active')


