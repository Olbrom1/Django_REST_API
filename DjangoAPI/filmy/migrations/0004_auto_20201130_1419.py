# Generated by Django 3.1.3 on 2020-11-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_film_plakat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='opis',
            field=models.TextField(),
        ),
    ]