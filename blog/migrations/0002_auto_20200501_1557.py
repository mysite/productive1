# Generated by Django 3.0.4 on 2020-05-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('slide', 'Slide'), ('picture', 'Picture'), ('project', 'Project'), ('album', 'Album')], default='no', max_length=10),
        ),
    ]
