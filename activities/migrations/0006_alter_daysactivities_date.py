# Generated by Django 4.2.4 on 2023-08-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0005_alter_daysactivities_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="daysactivities",
            name="date",
            field=models.DateField(),
        ),
    ]
