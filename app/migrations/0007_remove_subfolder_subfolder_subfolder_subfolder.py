# Generated by Django 4.2.3 on 2023-09-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_subfolder_subfolder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subfolder',
            name='subFolder',
        ),
        migrations.AddField(
            model_name='subfolder',
            name='subFolder',
            field=models.ManyToManyField(null=True, to='app.subfolder'),
        ),
    ]