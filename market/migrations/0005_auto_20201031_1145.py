# Generated by Django 3.1.2 on 2020-10-31 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20201031_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
