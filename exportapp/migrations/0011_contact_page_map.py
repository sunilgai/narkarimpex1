# Generated by Django 4.0.3 on 2022-03-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0010_contact_page_heading_alter_contact_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_page',
            name='map',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
