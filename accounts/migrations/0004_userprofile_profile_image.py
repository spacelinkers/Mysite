# Generated by Django 2.1.4 on 2019-01-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
