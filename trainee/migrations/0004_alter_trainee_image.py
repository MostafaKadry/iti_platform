# Generated by Django 5.1.7 on 2025-03-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0003_alter_trainee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
