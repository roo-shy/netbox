# Generated by Django 2.2 on 2019-07-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0073_interface_form_factor_to_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
    ]