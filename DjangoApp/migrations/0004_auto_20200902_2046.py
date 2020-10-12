# Generated by Django 3.1 on 2020-09-02 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0003_auto_20200824_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table1',
            old_name='field3',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='table1',
            old_name='field2',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='table1',
            name='field1',
        ),
        migrations.AddField(
            model_name='table1',
            name='user_id',
            field=models.IntegerField( verbose_name='userid'),
            preserve_default=False,
        ),
    ]