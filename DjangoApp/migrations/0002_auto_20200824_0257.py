# Generated by Django 3.1 on 2020-08-23 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1',
            name='field3',
            field=models.CharField(choices=[('p1', 'Project1'), ('p2', 'Project2'), ('p3', 'Project3'), ('p4', 'Project4')], default=django.utils.timezone.now, help_text='Select Project', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='table1',
            name='field1',
            field=models.CharField(help_text='Enter value', max_length=200),
        ),
    ]
