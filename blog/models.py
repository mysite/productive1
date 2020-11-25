from django.db import models
from datetime import datetime

class Category(models.Model):
    category=models.CharField('Category',max_length=200)
    description=models.CharField('Description',max_length=600)

    #def __str__(self):
    #    return self.category

class Blog_Entries(models.Model):
    title=models.CharField('Title',max_length=200)
    image = models.ImageField(upload_to="",
        null=True,
        blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank= True)
    tags = models.CharField('Tags', max_length=200, blank=True)   
    pub_date = models.DateTimeField('Published Date', default=datetime.now)	
    summary=models.TextField('Summary', blank=True)
    text1=models.TextField('Text1', blank=True)
    picture1= models.ImageField(upload_to="",
        null=True,
        blank=True)
    text2=models.TextField('Text2', blank=True)
    picture2= models.ImageField(upload_to="",
        null=True,
        blank=True)
    text3=models.TextField('Text3', blank=True)
    picture3= models.ImageField(upload_to="",
        null=True,
        blank=True)
    text4=models.TextField('Text4', blank=True)
    picture4= models.ImageField(upload_to="",
        null=True,
        blank=True)

    class Admin:
        list_display = (
            'title',
            'image',
            'category',
            'tags',
            'pub_date',
            'text1'
        )

    #def __unicode__(self):
    #    return str(self.title)
