# Generated by Django 3.1 on 2020-10-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0011_auto_20200908_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='field1',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='user Id'),
        ),
        migrations.AlterField(
            model_name='table1',
            name='field2',
            field=models.CharField(max_length=20, verbose_name='user Name'),
        ),
    ]
