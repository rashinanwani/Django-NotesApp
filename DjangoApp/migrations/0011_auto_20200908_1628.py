# Generated by Django 3.1 on 2020-09-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0010_auto_20200908_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewnotes',
            name='id',
        ),
        migrations.AddField(
            model_name='viewnotes',
            name='noteid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
