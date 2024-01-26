# Generated by Django 5.0.1 on 2024-01-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='feedback/')),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
