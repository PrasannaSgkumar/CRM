# Generated by Django 4.2.2 on 2024-01-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_app1', '0002_tag_orders_customer_orders_products_orders_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='tags',
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='New_app1.tag'),
        ),
    ]
