# Generated by Django 5.0.1 on 2024-03-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
