# Generated by Django 4.2.3 on 2023-09-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_subfolder_secondarybranchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainbranch',
            name='files',
            field=models.ManyToManyField(null=True, to='app.folderfiles'),
        ),
    ]