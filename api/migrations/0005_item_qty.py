# Generated by Django 3.2.21 on 2023-10-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20231004_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
