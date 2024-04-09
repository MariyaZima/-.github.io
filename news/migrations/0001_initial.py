# Generated by Django 5.0.2 on 2024-02-12 18:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_choice', models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], default='NE', max_length=2)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('rating_art_new', models.IntegerField(default=0)),
                ('one_to_many_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=1024)),
                ('comment_datetime', models.DateTimeField(auto_now_add=True)),
                ('comment_rating', models.IntegerField(default=0)),
                ('one_to_many_relation1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('one_to_many_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_to_many_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
                ('one_to_many_relation1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='many_to_many_relation',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
    ]
