# Generated by Django 3.1.2 on 2020-11-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20201031_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
