# Generated by Django 3.0.4 on 2020-03-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200311_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mask',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mask',
            name='stock_at',
            field=models.DateTimeField(null=True),
        ),
    ]
