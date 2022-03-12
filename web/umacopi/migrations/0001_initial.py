# Generated by Django 3.2.9 on 2022-02-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jockey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='騎手名')),
            ],
            options={
                'verbose_name_plural': '騎手',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=10, verbose_name='印の種類')),
            ],
            options={
                'verbose_name_plural': '印',
            },
        ),
        migrations.CreateModel(
            name='RaceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=12, verbose_name='開催日')),
            ],
            options={
                'verbose_name_plural': 'レース情報',
            },
        ),
        migrations.CreateModel(
            name='Stable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='厩舎名')),
            ],
            options={
                'verbose_name_plural': '厩舎',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='開催場所名')),
            ],
            options={
                'verbose_name_plural': '開催場所',
            },
        ),
        migrations.CreateModel(
            name='RaceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_num', models.CharField(blank=True, max_length=4, null=True, verbose_name='レース')),
                ('raceinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umacopi.raceinfo', verbose_name='レース情報')),
            ],
            options={
                'verbose_name_plural': '出馬表',
            },
        ),
        migrations.CreateModel(
            name='RaceResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='着順')),
                ('frame', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='枠')),
                ('umaban', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='馬番')),
                ('rev_umaban', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='逆番')),
                ('horse_name', models.CharField(max_length=10, verbose_name='馬名')),
                ('odds', models.FloatField(blank=True, null=True, verbose_name='単勝オッズ')),
                ('popularity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='人気')),
                ('jockey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umacopi.jockey', verbose_name='騎手')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umacopi.mark', verbose_name='印')),
                ('racetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umacopi.racetable', verbose_name='出馬表')),
                ('stable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umacopi.stable', verbose_name='厩舎')),
            ],
            options={
                'verbose_name_plural': 'レース結果',
            },
        ),
        migrations.AddField(
            model_name='raceinfo',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umacopi.venue', verbose_name='開催場所'),
        ),
    ]
