# Generated by Django 4.0.3 on 2022-03-22 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMemberMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
