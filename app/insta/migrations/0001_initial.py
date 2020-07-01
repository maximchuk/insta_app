# Generated by Django 3.0.7 on 2020-07-01 09:45

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_stuff', models.BooleanField(default=False)),
                ('birthday', models.DateField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstagramAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=250)),
                ('token_type', models.CharField(max_length=50)),
                ('expires_in', models.DateTimeField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instagram', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instagram account',
                'verbose_name_plural': 'Instagram accounts',
            },
        ),
    ]