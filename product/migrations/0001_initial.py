# Generated by Django 3.1.7 on 2021-03-20 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('condition', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
