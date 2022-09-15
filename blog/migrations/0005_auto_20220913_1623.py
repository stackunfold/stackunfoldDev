# Generated by Django 3.2.15 on 2022-09-13 10:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_jee_mains_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jee_mains',
            name='option_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=[], max_length=5000, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='jee_mains',
            name='question_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=[], max_length=5000, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='jee_mains',
            name='solution_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=[], max_length=5000, null=True), size=None),
        ),
    ]
