# Generated by Django 3.2.8 on 2021-10-20 15:18

from django.db import migrations, models
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformcategory',
            options={},
        ),
        migrations.AlterModelOptions(
            name='contactformcategorytranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'contact form category Translation'},
        ),
        migrations.AlterModelManagers(
            name='contactformcategory',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='contactformcategorytranslation',
            name='language_code',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='contactformcategorytranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='contact_form.contactformcategory'),
        ),
    ]