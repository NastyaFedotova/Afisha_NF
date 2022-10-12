# Generated by Django 4.1.1 on 2022-10-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0007_delete_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('event_title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
    ]
