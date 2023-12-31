# Generated by Django 4.2.7 on 2023-12-18 03:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pais",
            fields=[
                ("idpais", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=5, unique=True)),
                ("nombre", models.CharField(max_length=100)),
                ("poblacion", models.IntegerField()),
                ("estado", models.BooleanField()),
            ],
        ),
    ]
