# Generated by Django 3.2.6 on 2022-04-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportapp', '0025_auto_20220412_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='love_for_clients1',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='love_for_clients2',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='love_for_clients3',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='love_for_clients4',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='love_for_clients5',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]