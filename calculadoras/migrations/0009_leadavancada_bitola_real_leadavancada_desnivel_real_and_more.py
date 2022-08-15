# Generated by Django 4.1 on 2022-08-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadoras", "0008_alter_leadavancada_tipo_cabo"),
    ]

    operations = [
        migrations.AddField(
            model_name="leadavancada",
            name="bitola_real",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="desnivel_real",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="diametro_comercial",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="diametro_econ",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="perda_carga_conex_total",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="perda_carga_tub",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="perda_carga_unit",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="porcentagem_perda",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="leadavancada",
            name="vel_escoamento",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]