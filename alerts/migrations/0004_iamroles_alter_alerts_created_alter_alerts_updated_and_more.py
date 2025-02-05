# Generated by Django 5.1.4 on 2025-01-07 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_alerts_short_description_alter_alerts_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IAMRoles',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100, unique=True)),
                ('created', models.BigIntegerField(default=1736243274)),
                ('updated', models.BigIntegerField(default=1736243274)),
            ],
        ),
        migrations.AlterField(
            model_name='alerts',
            name='created',
            field=models.BigIntegerField(default=1736243274),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='updated',
            field=models.BigIntegerField(default=1736243274),
        ),
        migrations.CreateModel(
            name='IAMUsers',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('created', models.BigIntegerField(default=1736243274)),
                ('updated', models.BigIntegerField(default=1736243274)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.iamroles')),
            ],
        ),
    ]
