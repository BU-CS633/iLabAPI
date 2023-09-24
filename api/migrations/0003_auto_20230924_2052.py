# Generated by Django 3.2.21 on 2023-09-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230924_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vendor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='approved_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='order_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='received_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
