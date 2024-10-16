from django.contrib import admin
from .models import Profil, Produit, Categorie, Pays, ArticleDeBlog, Panier, Commande, ContactMessage

# Enregistrement des modèles existants
admin.site.register(Profil)
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Pays)
admin.site.register(ArticleDeBlog)
admin.site.register(Panier)
admin.site.register(Commande)

# Enregistrement du modèle ContactMessage avec configuration personnalisée
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'whatsapp_number', 'date_sent')
    search_fields = ('full_name', 'whatsapp_number')
    list_filter = ('date_sent',)
    ordering = ('-date_sent',)
