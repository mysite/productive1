from django.db import models
#from django.urls import reverse
#from django.utils.encoding import python_2_unicode_compatible

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    text = models.CharField(max_length=350)

    class Admin:
        list_display = (
            'name',
            'email',
            'subject',
            'Text'
        )
    
