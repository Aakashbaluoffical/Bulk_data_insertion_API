# Generated by Django 5.1.5 on 2025-02-02 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapi', '0003_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user_tbl',
        ),
    ]
