# Generated by Django 4.1.3 on 2022-11-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photo", "0003_alter_photo_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="URL",
            field=models.ImageField(
                help_text="URL to locally stored file", null=True, upload_to=""
            ),
        ),
    ]
