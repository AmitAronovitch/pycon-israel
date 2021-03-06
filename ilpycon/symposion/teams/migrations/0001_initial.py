# Generated by Django 2.0.1 on 2018-01-17 03:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('applied', 'applied'), ('invited', 'invited'), ('declined', 'declined'), ('rejected', 'rejected'), ('member', 'member'), ('manager', 'manager')], max_length=20, verbose_name='State')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('access', models.CharField(choices=[('open', 'open'), ('application', 'by application'), ('invitation', 'by invitation')], max_length=20, verbose_name='Access')),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='Created')),
                ('manager_permissions', models.ManyToManyField(blank=True, related_name='manager_teams', to='auth.Permission', verbose_name='Manager permissions')),
                ('permissions', models.ManyToManyField(blank=True, related_name='member_teams', to='auth.Permission', verbose_name='Permissions')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='teams.Team', verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
