# Generated by Django 4.1 on 2022-08-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadoras", "0006_leadbasica_potencia"),
    ]

    operations = [
        migrations.CreateModel(
            name="LeadAvancada",
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
                ("nome", models.CharField(max_length=50)),
                ("telefone", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.CharField(max_length=50)),
                (
                    "concessionaria",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("desnivel", models.IntegerField()),
                ("vazao", models.IntegerField()),
                ("dist_hidr", models.IntegerField()),
                ("dist_eletr", models.IntegerField()),
                (
                    "modelo",
                    models.CharField(
                        choices=[("On", "On Grid"), ("Off", "Off Grid")],
                        default="On",
                        max_length=10,
                    ),
                ),
                (
                    "tipo_cabo",
                    models.CharField(
                        choices=[("On", "On Grid"), ("Off", "Off Grid")],
                        default="A",
                        max_length=10,
                    ),
                ),
                ("potencia", models.IntegerField()),
                ("mchs", models.IntegerField()),
                ("data", models.DateField()),
            ],
        ),
    ]
