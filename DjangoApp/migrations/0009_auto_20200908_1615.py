# Generated by Django 3.1 on 2020-09-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0008_auto_20200905_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewnotes',
            name='id',
        ),
        migrations.AddField(
            model_name='viewnotes',
            name='noteid',
            field=models.AutoField(default=1, serialize=False),
            preserve_default=False,
        ),
    ]
