# Generated by Django 3.0.2 on 2020-02-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exsel', '0002_auto_20200201_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['published'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='product',
            name='composition',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Состав'),
        ),
    ]
