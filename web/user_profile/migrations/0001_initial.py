# Generated by Django 4.2 on 2023-04-30 14:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoDriver',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=13, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('eng', 'English'), ('hin', 'Hindi'), ('kan', 'Kannada'), ('pun', 'Punjabi')], default='eng', max_length=3)),
                ('registeration_number', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=13, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('eng', 'English'), ('hin', 'Hindi'), ('kan', 'Kannada'), ('pun', 'Punjabi')], default='eng', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='AutoDriverLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lonitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.autodriver')),
            ],
        ),
    ]
