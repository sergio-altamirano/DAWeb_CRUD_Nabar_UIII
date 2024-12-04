# Generated by Django 5.1.3 on 2024-11-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('id_producto', models.SmallIntegerField()),
                ('id_cliente', models.SmallIntegerField()),
                ('fecha_venta', models.DateField()),
                ('id_sucursal', models.SmallIntegerField()),
                ('cantidad', models.SmallIntegerField()),
                ('pago', models.CharField(max_length=50)),
            ],
        ),
    ]