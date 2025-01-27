# Generated by Django 5.1.4 on 2025-01-06 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test__', '0002_customertype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_fathers_name', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=500)),
                ('customer_contact_number', models.CharField(max_length=10)),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_IP', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_created_by_set', to=settings.AUTH_USER_MODEL)),
                ('customerType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_customer_type', to='test__.customertype')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_updated_by_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['customer_id'],
            },
        ),
    ]
