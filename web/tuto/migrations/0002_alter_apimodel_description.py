# Generated by Django 4.1.3 on 2022-12-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimodel',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
