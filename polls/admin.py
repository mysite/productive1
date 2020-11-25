from django.contrib import admin

from .models import Contact, Newsletter#, Pictures

#admin.site.register(Picture)
#class PictureAdmin(admin.ModelAdmin):
#    list_display = ('title', 'text', 'category','pub_date')

#admin.site.register(Pictures, PictureAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','text')


admin.site.register(Contact, ContactAdmin)

admin.site.register(Newsletter)
