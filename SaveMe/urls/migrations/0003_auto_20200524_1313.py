# Generated by Django 3.0.6 on 2020-05-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0002_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='te2.jpg', upload_to='urls/', verbose_name='Картинка'),
        ),
    ]
