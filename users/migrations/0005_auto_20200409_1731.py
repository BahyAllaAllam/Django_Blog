# Generated by Django 3.0.4 on 2020-04-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200409_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics/'),
        ),
    ]
