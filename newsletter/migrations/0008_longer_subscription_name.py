# Generated by Django 3.1.2 on 2020-10-28 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_switch_from_sorl_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='name_field',
            field=models.CharField(blank=True, db_column='name', help_text='optional', max_length=200, null=True, verbose_name='name'),
        ),
    ]
