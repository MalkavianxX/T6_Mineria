# Generated by Django 4.0.1 on 2022-01-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_alter_venta_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='id',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]