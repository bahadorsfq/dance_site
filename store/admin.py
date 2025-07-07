from django.contrib import admin
from .models import Package, OrientalMusic, UserPackage  

admin.site.register(OrientalMusic)
admin.site.register(UserPackage)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    fields = ('title', 'description', 'price', 'cover_image', 'video_file','video_url', 'is_active')



