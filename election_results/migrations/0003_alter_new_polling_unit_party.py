# Generated by Django 4.0 on 2022-01-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election_results', '0002_new_polling_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_polling_unit',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='election_results.party'),
        ),
    ]
