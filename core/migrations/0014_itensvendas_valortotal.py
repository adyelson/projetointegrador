# Generated by Django 4.2 on 2023-05-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_vendas_datavenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='itensvendas',
            name='valorTotal',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]