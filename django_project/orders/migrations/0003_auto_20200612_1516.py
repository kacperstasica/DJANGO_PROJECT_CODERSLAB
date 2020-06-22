# Generated by Django 3.0.6 on 2020-06-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200612_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ED', 'edit'), ('AO', 'awaiting order'), ('PS', 'payment success'), ('PF', 'payment failed')], default='ED', max_length=15),
        ),
    ]
