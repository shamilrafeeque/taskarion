# Generated by Django 4.1.4 on 2022-12-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmainmodel',
            name='Size',
            field=models.CharField(choices=[('10', '10'), ('20', '20'), ('30', '30')], max_length=20),
        ),
    ]
