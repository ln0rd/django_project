# Generated by Django 3.1.4 on 2021-01-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201220_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='Sobre o Curso'),
        ),
    ]
