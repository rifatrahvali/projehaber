from django.contrib import admin
from django.http import HttpRequest
from .models import *
# Register your models here.




# - Haber 
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category',)

# - Kategori
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


# - Galeri
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','image',)

# - hakkımızda
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj=None):
        return False

# - iletişim
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullName','phone','email','message')

# - Duyurular
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    group_fieldsets = True
# - Ayarlar
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request,obj=None):
        return False