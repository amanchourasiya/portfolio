# Generated by Django 3.0.8 on 2020-07-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('blog_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('blog_view_count', models.IntegerField()),
            ],
            options={
                'db_table': 'post_views',
            },
        ),
    ]
