# Generated by Django 5.0.1 on 2024-01-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=7)),
                ('phone_number', models.IntegerField(blank=True, unique=True)),
                ('country', models.CharField(blank=True, max_length=127, null=True)),
                ('city', models.CharField(blank=True, max_length=127, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
