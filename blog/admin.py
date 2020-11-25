from django.contrib import admin

from .models import Blog_Entries, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title'
    		,'image'
    		,'category'
            ,'tags'
            ,'pub_date'
            ,'summary'
            ,'text1')

admin.site.register(Blog_Entries, BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','description')

admin.site.register(Category, CategoryAdmin)
