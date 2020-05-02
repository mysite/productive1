from django.db import models
from datetime import datetime

class Category(models.Model):
    category=models.CharField('Category',max_length=200)
    description=models.CharField('Description',max_length=600)

    def __str__(self):
        return self.category

class Blog_Entries(models.Model):
    title=models.CharField('Title',max_length=200)
    image = models.ImageField(upload_to="",
        null=True,
        blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank= True)
    tags = models.CharField('Tags', max_length=200, blank=True)   
    pub_date = models.DateTimeField('Published Date', default=datetime.now)	
    summary=models.TextField('Text', blank=True)
    text=models.TextField('Text', blank=True)
    
    class Admin:
        list_display = (
            'title',
            'image',
            'category',
            'tags',
            'pub_date',
            'text'
        )
    def __unicode__(self):
        return str(self.title)