# Generated by Django 3.2.3 on 2021-06-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20210602_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]