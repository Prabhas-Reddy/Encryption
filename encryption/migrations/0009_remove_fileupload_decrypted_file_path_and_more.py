# Generated by Django 5.1.3 on 2024-12-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0008_alter_audiofile_uploaded_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='decrypted_file_path',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='encrypted_file_path',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='decrypted_file',
            field=models.FileField(blank=True, null=True, upload_to='decrypted_files/'),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='encrypted_file',
            field=models.FileField(blank=True, null=True, upload_to='encrypted_files/'),
        ),
    ]
