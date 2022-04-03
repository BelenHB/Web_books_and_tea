# Generated by Django 4.0.3 on 2022-04-01 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_page_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha creación'),
        ),
    ]