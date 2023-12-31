# Generated by Django 4.2.7 on 2023-12-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TicketBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(
                        help_text="Enter a valid email address.",
                        max_length=254,
                        unique=True,
                        verbose_name="Email Address",
                    ),
                ),
                (
                    "countryName",
                    models.CharField(
                        max_length=100, verbose_name="Write your country name"
                    ),
                ),
                (
                    "pfrom",
                    models.CharField(
                        max_length=100, verbose_name="Write your depature airport name"
                    ),
                ),
                (
                    "pto",
                    models.CharField(
                        max_length=100, verbose_name="Write your arriavle airport name"
                    ),
                ),
                ("depatureDate", models.DateTimeField(verbose_name="Departure Date")),
                ("returnDate", models.DateField(verbose_name="Return Date")),
                (
                    "chosen_option",
                    models.CharField(
                        choices=[("oneway", "Oneway"), ("roundway", "Round")],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
