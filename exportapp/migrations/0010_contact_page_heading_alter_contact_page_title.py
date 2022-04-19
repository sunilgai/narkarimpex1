# Generated by Django 4.0.3 on 2022-03-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0009_alter_contact_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_page',
            name='heading',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact_page',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]