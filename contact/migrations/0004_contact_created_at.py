# Generated by Django 4.2.4 on 2023-10-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_message_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
