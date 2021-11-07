# Generated by Django 2.1.1 on 2021-11-07 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0009_auto_20211106_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('authenticator', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='experiment.User')),
            ],
        ),
    ]
