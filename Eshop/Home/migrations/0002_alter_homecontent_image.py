# Generated by Django 3.2.6 on 2021-11-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='image',
            field=models.FileField(max_length=250, upload_to='homecontent/'),
        ),
    ]
