# Generated by Django 4.2.2 on 2023-07-19 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=50)),
                ('account_number', models.PositiveIntegerField()),
                ('expiry_date', models.DateField()),
                ('is_default', models.BooleanField(default=False)),
                ('payment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.paymenttype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
