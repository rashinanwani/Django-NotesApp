# Generated by Django 3.1 on 2020-09-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0007_auto_20200902_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='viewnotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=200, verbose_name='notes')),
            ],
        ),
        migrations.DeleteModel(
            name='table2',
        ),
        migrations.RemoveField(
            model_name='table1',
            name='id',
        ),
        migrations.AlterField(
            model_name='table1',
            name='field1',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='user id'),
        ),
    ]