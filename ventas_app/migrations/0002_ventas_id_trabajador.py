# Generated by Django 5.1 on 2024-12-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='id_trabajador',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]