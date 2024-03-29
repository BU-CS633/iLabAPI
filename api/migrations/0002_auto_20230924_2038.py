# Generated by Django 3.2.21 on 2023-09-24 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

 dependencies = [
     migrations.swappable_dependency(settings.AUTH_USER_MODEL),
     ('api', '0001_initial'),
 ]

 operations = [
     migrations.CreateModel(
         name='Status',
         fields=[
             ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
             ('description', models.CharField(max_length=200, null=True)),
         ],
     ),
     migrations.RenameField(
         model_name='item',
         old_name='item_name',
         new_name='name',
     ),
     migrations.AddField(
         model_name='item',
         name='qty',
         field=models.IntegerField(default=0),
         preserve_default=False,
     ),
     migrations.AddField(
         model_name='item',
         name='vendor',
         field=models.CharField(max_length=200, null=True),
     ),
     migrations.CreateModel(
         name='Request',
         fields=[
             ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
             ('request_date', models.DateField(null=True)),
             ('order_date', models.DateField(null=True)),
             ('received_date', models.DateField(null=True)),
             ('approved_date', models.DateField(null=True)),
             ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
             ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
             ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.status')),
         ],
     ),
 ]