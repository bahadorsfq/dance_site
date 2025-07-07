from django.contrib import admin
from .models import Package, OrientalMusic, UserPackage, Purchase

admin.site.register(OrientalMusic)
admin.site.register(UserPackage)
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'purchase_date')
    list_filter = ('package', 'purchase_date')
    search_fields = ('user__username', 'package__title')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    fields = ('title', 'description', 'price', 'cover_image', 'video_file','video_url', 'is_active')



