# Generated by Django 2.0.7 on 2018-08-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_heading', models.CharField(max_length=250)),
                ('article_body', models.TextField()),
            ],
        ),
    ]
