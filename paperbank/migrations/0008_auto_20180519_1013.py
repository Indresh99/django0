# Generated by Django 2.0.3 on 2018-05-19 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paperbank', '0007_auto_20180519_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bca',
            old_name='bca_link',
            new_name='bca_link_mid',
        ),
        migrations.RenameField(
            model_name='biotech',
            old_name='biotech_link',
            new_name='biotech_link_mid',
        ),
        migrations.RenameField(
            model_name='civil',
            old_name='civil_link',
            new_name='civil_link_mid',
        ),
        migrations.RenameField(
            model_name='cse',
            old_name='cse_link',
            new_name='cse_link_mid',
        ),
        migrations.RenameField(
            model_name='electronics',
            old_name='electronics_link',
            new_name='electronics_link_mid',
        ),
        migrations.RenameField(
            model_name='it',
            old_name='it_link',
            new_name='it_link_mid',
        ),
        migrations.RenameField(
            model_name='mech',
            old_name='mech_link',
            new_name='mech_link_mid',
        ),
    ]