# Generated by Django 3.1 on 2020-10-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0012_auto_20201012_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewnotes',
            name='user',
            field=models.CharField(default='rashi', max_length=30, verbose_name='user'),
            preserve_default=False,
        ),
    ]
