# Generated by Django 4.1 on 2022-08-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadoras", "0003_alter_leadbasica_mchs_alter_leadbasica_potencia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leadbasica",
            name="mchs",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="leadbasica",
            name="potencia",
            field=models.IntegerField(null=True),
        ),
    ]