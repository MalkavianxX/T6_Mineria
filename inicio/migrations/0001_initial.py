# Generated by Django 4.0.1 on 2022-01-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
