# Generated by Django 2.1.4 on 2020-03-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connectoon', '0006_auto_20200320_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.IntegerField(default=0)),
                ('image', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebToon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('story', models.TextField(blank=True)),
                ('style', models.TextField(blank=True)),
                ('thumbnail_story', models.TextField(blank=True)),
                ('thumbnail_style', models.TextField(blank=True)),
                ('like', models.IntegerField(default=0)),
                ('create_date', models.TextField(blank=True)),
                ('genre', models.TextField(blank=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='connectoon.Author')),
            ],
        ),
        migrations.AddField(
            model_name='toon',
            name='webtoon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='connectoon.WebToon'),
        ),
    ]
