# Generated by Django 5.1.1 on 2024-11-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
