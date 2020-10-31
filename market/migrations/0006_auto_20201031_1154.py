# Generated by Django 3.1.2 on 2020-10-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20201031_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]