# Generated by Django 3.0.6 on 2020-06-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=140, verbose_name='name')),
                ('description', models.TextField(blank=True, default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('alcohol', models.DecimalField(decimal_places=1, max_digits=3)),
                ('image', models.ImageField(default='default_beer.jpg', upload_to='beer_labels')),
            ],
            options={
                'verbose_name': 'Piwsko',
                'verbose_name_plural': 'Piwska',
            },
        ),
    ]
