# Generated by Django 5.1.3 on 2024-12-23 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0013_audioupload_imagehistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audioupload',
            old_name='decrypted_audio',
            new_name='decrypted_file',
        ),
        migrations.RenameField(
            model_name='audioupload',
            old_name='encrypted_audio',
            new_name='encrypted_file',
        ),
        migrations.RenameField(
            model_name='audioupload',
            old_name='audio',
            new_name='file',
        ),
    ]
