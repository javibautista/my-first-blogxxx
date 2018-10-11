# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('apellido', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200, default='')),
                ('edad', models.CharField(max_length=200)),
                ('fech_nac', models.DateTimeField(blank=True, null=True)),
                ('alta', models.DateTimeField(default=django.utils.timezone.now)),
                ('persona', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
