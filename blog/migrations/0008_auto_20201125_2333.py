# Generated by Django 3.0.4 on 2020-11-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201109_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_entries',
            name='summary',
            field=models.TextField(blank=True, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='blog_entries',
            name='text1',
            field=models.TextField(blank=True, verbose_name='Text1'),
        ),
        migrations.AlterField(
            model_name='blog_entries',
            name='text2',
            field=models.TextField(blank=True, verbose_name='Text2'),
        ),
        migrations.AlterField(
            model_name='blog_entries',
            name='text3',
            field=models.TextField(blank=True, verbose_name='Text3'),
        ),
        migrations.AlterField(
            model_name='blog_entries',
            name='text4',
            field=models.TextField(blank=True, verbose_name='Text4'),
        ),
    ]
