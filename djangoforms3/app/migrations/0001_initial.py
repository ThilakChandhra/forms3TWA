# Generated by Django 3.2.18 on 2023-04-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
