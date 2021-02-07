from django.contrib import admin

#from .models import Products

#class ListingAdmin(admin.ModelAdmin):
#    list_display = ('title', 'in_stock', 'price', 'description','sold')

# Register your models here.
#admin.site.register(Products)

from .models import Products, PostImage
 
class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Products
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
