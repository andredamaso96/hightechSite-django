# Generated by Django 3.0.8 on 2020-07-22 11:00

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('type_job', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('work_time', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('responsabilities', jsonfield.fields.JSONField(default=dict)),
                ('qualifications', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
