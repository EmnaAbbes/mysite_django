# Generated by Django 4.1.7 on 2023-02-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='Img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]