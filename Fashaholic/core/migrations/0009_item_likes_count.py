# Generated by Django 3.0.7 on 2022-05-27 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_weights'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
