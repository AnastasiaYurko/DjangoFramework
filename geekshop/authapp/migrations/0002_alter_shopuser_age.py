# Generated by Django 3.2.8 on 2021-11-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='Возраст'),
        ),
    ]