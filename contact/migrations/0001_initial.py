# Generated by Django 4.2.4 on 2023-10-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField()),
                ('Email', models.TextField()),
                ('Subject', models.TextField()),
                ('Message', models.FileField(upload_to='')),
            ],
        ),
    ]
