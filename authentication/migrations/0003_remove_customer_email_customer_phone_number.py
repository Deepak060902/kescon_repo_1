# Generated by Django 5.0.3 on 2024-03-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_customer_name_customer_billing_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
