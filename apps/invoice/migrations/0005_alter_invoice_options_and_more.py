# Generated by Django 5.0.3 on 2024-04-08 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_rename_invocie_item_invoice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='client_place',
            new_name='client_province',
        ),
    ]
