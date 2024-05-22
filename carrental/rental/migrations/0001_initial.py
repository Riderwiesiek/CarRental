# Generated by Django 5.0.3 on 2024-05-08 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('engine_type', models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20)),
                ('seats_count', models.PositiveSmallIntegerField()),
                ('dors_count', models.PositiveSmallIntegerField()),
                ('fuel_usage', models.FloatField()),
                ('engine_power', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('gearbox_type', models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20)),
                ('available', models.BooleanField()),
                ('equipment', models.ManyToManyField(to='rental.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('declared_order_duration', models.DurationField()),
                ('pickup_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('karta', 'Karta'), ('gotowka', 'Gotowka'), ('przelew', 'Przelew'), ('blik', 'Blik')], max_length=20)),
                ('payment_status', models.BooleanField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rental.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rental.user')),
            ],
        ),
    ]
