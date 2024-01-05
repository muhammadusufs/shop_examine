# Generated by Django 5.0.1 on 2024-01-05 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_admins',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.shop'),
        ),
    ]
