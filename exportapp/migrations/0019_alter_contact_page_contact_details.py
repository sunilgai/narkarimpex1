# Generated by Django 4.0.3 on 2022-04-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0018_delete_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_page',
            name='Contact_details',
            field=models.CharField(max_length=100),
        ),
    ]