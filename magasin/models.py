from django.db import models
from datetime import date
# Create your models here.
class Produit(models.Model):
    TYPE_CHOICES=[('fr','frais'),('cs','conserve'),('em','emballé')]
    libelle=models.CharField(max_length=255)
    desciption=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    Img=models.ImageField(blank=True)
    categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libelle+" "+self.desciption+" "+str(self.prix)+" "+str(self.type)
class Categorie(models.Model):
    TYPE_CHOICES=[('Al','Alimentaire'), ('Mb','Meuble'),('Sn','Sanitaire'), ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(max_length=2,choices=TYPE_CHOICES,default='Al')
    def __str__(self):
        return self.name
class Fournisseur(models.Model):
    name=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.name
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=10)
    def __str__(self):
        return super().__str__()+" "+self.Duree_garantie
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        return str(self.dateCde)+" "+str(self.totalCde)


