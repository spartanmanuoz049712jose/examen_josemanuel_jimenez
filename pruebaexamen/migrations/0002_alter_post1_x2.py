# Generated by Django 4.1 on 2022-09-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaexamen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='x2',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
