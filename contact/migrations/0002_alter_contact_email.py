# Generated by Django 4.2.4 on 2023-10-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
