# Generated by Django 4.1.7 on 2023-03-01 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('produit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magasin.produit')),
                ('Duree_garantie', models.CharField(max_length=10)),
            ],
            bases=('magasin.produit',),
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCde', models.DateField(default=datetime.date.today, null=True)),
                ('totalCde', models.DecimalField(decimal_places=3, max_digits=10)),
                ('produits', models.ManyToManyField(to='magasin.produit')),
            ],
        ),
    ]
