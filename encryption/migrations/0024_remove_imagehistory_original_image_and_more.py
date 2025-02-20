# Generated by Django 5.1.3 on 2024-12-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0023_rename_decrypted_image_imagehistory_decrypted_image_base64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagehistory',
            name='original_image',
        ),
        migrations.AddField(
            model_name='imagehistory',
            name='encrypted_image',
            field=models.ImageField(blank=True, null=True, upload_to='encrypted_images/'),
        ),
        migrations.AlterField(
            model_name='imagehistory',
            name='decrypted_image_base64',
            field=models.TextField(blank=True, null=True),
        ),
    ]
