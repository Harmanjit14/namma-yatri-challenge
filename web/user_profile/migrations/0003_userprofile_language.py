# Generated by Django 4.2 on 2023-04-07 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('eng', 'English'), ('hin', 'Hindi'), ('kan', 'Kannada'), ('pun', 'Punjabi')], default='eng', max_length=3),
        ),
    ]