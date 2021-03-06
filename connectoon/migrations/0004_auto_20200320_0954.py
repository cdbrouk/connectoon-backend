# Generated by Django 2.1.4 on 2020-03-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connectoon', '0003_auto_20200320_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='career',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='connectoon.Author'),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='create_date',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='story',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='style',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='thumbnail_story',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='thumbnail_style',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='webtoon',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
