# Generated by Django 5.1.3 on 2024-11-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
