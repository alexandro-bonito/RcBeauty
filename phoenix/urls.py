
from django.urls import path
from . import views


urlpatterns = [



    path('', views.home, name='home'),
    path('ajouter-produit/', views.ajouter_produit, name='ajouter_produit'),
    path('ajouter-article/', views.ajouter_article, name='ajouter_article'),
    path('ajouter-categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('admin_pannele', views.admin_pannele, name='admin_pannele'),
    path('ajouter-pays/', views.ajouter_pays, name='ajouter_pays'),
    path('blog/', views.blog_posts, name='blog_posts'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/<int:article_id>/', views.blog_detail, name='blog_detail'),
    path('produits/', views.produits_par_categorie, name='produits_par_categorie'),
    path('signup/', views.signup, name='signup'),  # Route pour l'inscription
    path('signin/', views.signin, name='signin'),
    path('propos/', views.propos, name='propos'),# Route pour la connexion
    path('profil/', views.afficher_profil, name='afficher_profil'),
    path('produit/<int:produit_id>/', views.produit_detail, name='produit_detail'),
    path('ajouter-avis/', views.ajouter_avis, name='ajouter_avis'),
    path('panier/supprimer/<int:produit_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.afficher_panier, name='afficher_panier'),
    path('admin_pannele/', views.admin_pannele, name='admin_pannele'),
    path('produit/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('article/supprimer/<int:article_id>/', views.supprimer_article_blog, name='supprimer_article_blog'),

]
