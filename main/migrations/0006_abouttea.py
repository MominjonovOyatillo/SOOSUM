# Generated by Django 4.1.7 on 2023-03-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_advice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abouttea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_ru', models.CharField(max_length=255)),
                ('question_uz', models.CharField(max_length=255)),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
            ],
        ),
    ]
