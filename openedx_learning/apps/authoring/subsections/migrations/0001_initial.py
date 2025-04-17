# Generated by Django 4.2.19 on 2025-04-09 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oel_publishing', '0005_alter_entitylistrow_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('container', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oel_publishing.container')),
            ],
            options={
                'abstract': False,
            },
            bases=('oel_publishing.container',),
        ),
        migrations.CreateModel(
            name='SubsectionVersion',
            fields=[
                ('container_version', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oel_publishing.containerversion')),
            ],
            options={
                'abstract': False,
            },
            bases=('oel_publishing.containerversion',),
        ),
    ]
