# Generated by Django 2.1.2 on 2018-11-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingPortalApp', '0010_medicine_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='manufacturedBy',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='price',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]