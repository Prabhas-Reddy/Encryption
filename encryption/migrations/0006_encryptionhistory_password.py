# Generated by Django 5.1.3 on 2024-12-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryption', '0005_fileupload_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='encryptionhistory',
            name='password',
            field=models.CharField(default='default_password', max_length=100),
        ),
    ]
