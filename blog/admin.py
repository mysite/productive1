from django.contrib import admin

from .models import Blog_Entries, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title'
<<<<<<< HEAD
    		,'image'
=======
    		, 'image'
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
    		,'category'
            ,'tags'
            ,'pub_date'
            ,'summary'
<<<<<<< HEAD
            ,'text1')
=======
            ,'text')
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f

admin.site.register(Blog_Entries, BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','description')

admin.site.register(Category, CategoryAdmin)
