# Generated by Django 4.0.5 on 2022-07-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_create_date_alter_contact_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='customer_needs',
            new_name='customer_need',
        ),
    ]
