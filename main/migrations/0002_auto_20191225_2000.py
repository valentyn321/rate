# Generated by Django 2.2.6 on 2019-12-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='purchase',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='currency',
            name='selling',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
