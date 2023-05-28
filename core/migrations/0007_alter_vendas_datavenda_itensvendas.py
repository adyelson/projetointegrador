# Generated by Django 4.2 on 2023-05-27 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_produtos_vendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='dataVenda',
            field=models.DateField(verbose_name='Data Venda'),
        ),
        migrations.CreateModel(
            name='ItensVendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.produtos')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.vendas')),
            ],
        ),
    ]
