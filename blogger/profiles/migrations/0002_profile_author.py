# Generated by Django 4.2.7 on 2023-12-07 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("author", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="author.author",
            ),
        ),
    ]
