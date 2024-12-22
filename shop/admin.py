from django.contrib import admin
from shop.models import Category, Item, Tag, Image  
from django.contrib.contenttypes.admin import GenericTabularInline  


class ImageInline(GenericTabularInline):
    model = Image
    extra = 1  


class ItemInline(admin.TabularInline):  
    model = Item
    extra = 1  


class TagInline(admin.StackedInline):  
    model = Item.tags.through 
    extra = 1 

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description') 
    search_fields = ('name', 'description') 
    ordering = ('-price',) 
    inlines = [TagInline, ImageInline] 

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',) 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',) 
    ordering = ('name',) 
    inlines = [ItemInline, ImageInline] 



admin.site.register(Image) 
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)



