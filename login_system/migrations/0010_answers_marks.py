# Generated by Django 3.1.3 on 2020-12-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0009_auto_20201207_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
