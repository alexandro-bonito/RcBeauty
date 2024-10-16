from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Pays(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.nom

class Profil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    numero_whatsapp = models.CharField(max_length=15)
    pays = models.ForeignKey(Pays, null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)  # Ajout du champ photo
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    origine = models.ForeignKey(Pays, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()  # Ajout du champ description
    prix_commercial = models.DecimalField(max_digits=10, decimal_places=2)
    prix_partenaire = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produits/')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class ArticleDeBlog(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)  # Ajout de l'image
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Panier(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.profil} - {self.produit}"

class Commande(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande {self.id} - {self.panier.profil}"


# models.py
from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=15)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.full_name} - {self.date_sent.strftime('%Y-%m-%d %H:%M:%S')}"
from django.db import models
from django.conf import settings

from django.db import models
from django.conf import settings

class Avis(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    commentaire = models.TextField()
    note = models.PositiveIntegerField()  # Note sur une échelle de 1 à 5, par exemple
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis de {self.profil} - {self.commentaire[:20]}..."
