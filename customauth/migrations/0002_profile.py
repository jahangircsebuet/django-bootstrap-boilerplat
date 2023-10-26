# Generated by Django 4.0.3 on 2022-04-02 20:09

import customauth.models.profile
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=customauth.models.profile.avatar_upload_path)),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Bio')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]