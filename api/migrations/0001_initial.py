# Generated by Django 3.2.21 on 2023-09-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

 initial = True

 dependencies = [
 ]

 operations = [
     migrations.CreateModel(
         name='Item',
         fields=[
             ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
             ('item_name', models.CharField(max_length=200)),
         ],
     ),
 ]