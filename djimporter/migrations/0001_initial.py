# Generated by Django 3.0.4 on 2020-05-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'CREATED'), ('running', 'RUNNING'), ('failed', 'FAILED'), ('completed', 'COMPLETED')], max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=50)),
                ('errors', models.TextField(blank=True)),
                ('num_rows', models.IntegerField(null=True)),
                ('input_file', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]