# Generated by Django 5.0.3 on 2024-04-02 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_rename_invocie_item_invoice_is_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='invocie',
            new_name='invoice',
        ),
    ]
