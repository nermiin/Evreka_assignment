# Generated by Django 3.1.7 on 2021-03-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Q2', '0002_auto_20210315_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='bin',
            field=models.ManyToManyField(to='Q2.Bin'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='operation',
            field=models.ManyToManyField(to='Q2.Operation'),
        ),
    ]
