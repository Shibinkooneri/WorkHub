# Generated by Django 5.0.6 on 2024-06-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
                ('profilepic', models.ImageField(upload_to='customer_pics')),
            ],
        ),
    ]
