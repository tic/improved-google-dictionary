# Generated by Django 3.0.3 on 2021-11-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_o1',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_o2',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_o3',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_o4',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_o5',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_r1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_r2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_r3',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_r4',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_r5',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_t1',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_t2',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_t3',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_t4',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_t5',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_t6',
            field=models.TimeField(blank=True),
        ),
    ]
