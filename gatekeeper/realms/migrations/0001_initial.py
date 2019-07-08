# Generated by Django 2.1.5 on 2019-04-20 19:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slot', models.IntegerField()),
                ('read_key', models.CharField(max_length=32)),
                ('auth_key', models.CharField(max_length=32)),
                ('update_key', models.CharField(max_length=32)),
                ('public_key', models.TextField(help_text='public key in X.509 PEM format')),
                ('private_key', models.TextField(help_text='private key in X.509 PEM format')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
