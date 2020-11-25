from django.contrib import admin

<<<<<<< HEAD
from .models import Contact, Newsletter#, Pictures
=======
from .models import Contact #, Pictures
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f

#admin.site.register(Picture)
#class PictureAdmin(admin.ModelAdmin):
#    list_display = ('title', 'text', 'category','pub_date')

#admin.site.register(Pictures, PictureAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','text')

<<<<<<< HEAD
admin.site.register(Contact, ContactAdmin)

admin.site.register(Newsletter)
=======
admin.site.register(Contact, ContactAdmin)
>>>>>>> 077e043e98c2e6964d96bb90fe3f0e59a5e4307f
