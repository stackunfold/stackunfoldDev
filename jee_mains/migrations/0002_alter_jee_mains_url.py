# Generated by Django 3.2.15 on 2022-09-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jee_mains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jee_mains',
            name='url',
            field=models.SlugField(default='', max_length=1000, null=True),
        ),
    ]