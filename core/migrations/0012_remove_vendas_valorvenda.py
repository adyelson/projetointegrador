# Generated by Django 4.2 on 2023-05-28 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_produtos_cest_remove_produtos_codbarras_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='valorVenda',
        ),
    ]
