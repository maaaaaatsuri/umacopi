# Generated by Django 3.2.9 on 2022-01-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('held_date', models.CharField(max_length=12, verbose_name='開催日')),
                ('venue', models.CharField(max_length=10, verbose_name='開催場所')),
                ('race_number', models.CharField(max_length=4, verbose_name='レース')),
                ('rank', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='着順')),
                ('frame', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='枠')),
                ('umaban', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='馬番')),
                ('rev_umaban', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='逆番')),
                ('mark', models.CharField(max_length=6, verbose_name='印')),
                ('horse_name', models.CharField(max_length=10, verbose_name='馬名')),
                ('jockey', models.CharField(max_length=10, verbose_name='騎手')),
                ('stable', models.CharField(max_length=10, verbose_name='厩舎')),
                ('odds', models.FloatField(blank=True, null=True, verbose_name='単勝オッズ')),
                ('popularity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='人気')),
            ],
        ),
    ]
