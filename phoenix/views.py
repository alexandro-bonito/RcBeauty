from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import Produit, ArticleDeBlog

from django.shortcuts import render
from .models import Produit, ArticleDeBlog,Panier,Profil

from django.contrib.auth.decorators import login_required



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produit, ArticleDeBlog, Avis, Panier, Profil

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produit, ArticleDeBlog, Avis, Panier, Profil

from django.shortcuts import render
from .models import Produit, ArticleDeBlog, Avis, Panier

def home(request):
    # Récupérer les deux derniers produits et les deux derniers articles de blog
    derniers_produits = Produit.objects.order_by('-date_creation')[:2]
    derniers_articles = ArticleDeBlog.objects.order_by('-date_creation')[:2]
    avis_list = Avis.objects.order_by('-date_creation')[:5]  # Ajustez le nombre selon vos besoins

    # Calculer le nombre d'articles dans le panier
    panier_items = Panier.objects.all()  # Récupère tous les paniers sans filtrer par profil
    nombre_produits_panier = panier_items.count()

    context = {
        'derniers_produits': derniers_produits,
        'derniers_articles': derniers_articles,
        'avis_list': avis_list,
        'nombre_produits_panier': nombre_produits_panier,
    }

    return render(request, 'home.html', context)



from django.shortcuts import render, redirect
from .models import Produit, Categorie, Pays
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render, redirect
from .models import Produit, Categorie, Pays
from django.contrib import messages

def ajouter_produit(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        categorie_id = request.POST.get('categorie')
        prix_commercial = request.POST.get('prix_commercial')
        prix_partenaire = request.POST.get('prix_partenaire')
        origine_id = request.POST.get('origine')
        image = request.FILES.get('image')

        categorie = Categorie.objects.get(id=categorie_id)
        origine = Pays.objects.get(id=origine_id)

        produit = Produit(
            nom=nom,
            description=description,
            categorie=categorie,
            prix_commercial=prix_commercial,
            prix_partenaire=prix_partenaire,
            origine=origine,
            image=image
        )
        produit.save()
        messages.success(request, 'Produit ajouté avec succès.')
        return redirect('admin_pannele')  # Remplace par la vue souhaitée après l'ajout du produit

    categories = Categorie.objects.all()
    pays = Pays.objects.all()

    return render(request, 'product_ajout.html', {'categories': categories, 'pays': pays})



from .models import ArticleDeBlog
from django.shortcuts import render, redirect
from .models import ArticleDeBlog, Categorie
from django.contrib import messages

def ajouter_article(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        categorie_id = request.POST.get('categorie')
        image = request.FILES.get('image')

        categorie = Categorie.objects.get(id=categorie_id)

        article = ArticleDeBlog(
            titre=titre,
            description=description,
            categorie=categorie,
            image=image
        )
        article.save()
        messages.success(request, 'Article ajouté avec succès.')
        return redirect('admin_pannele')  # Remplace par la vue souhaitée après l'ajout de l'article

    categories = Categorie.objects.all()

    return render(request, 'ajouter_article.html', {'categories': categories})


from django.shortcuts import render, redirect
from .models import Categorie
from django.contrib import messages

def ajouter_categorie(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        categorie = Categorie(nom=nom)
        categorie.save()
        messages.success(request, 'Catégorie ajoutée avec succès.')
        return redirect('admin_pannele')  # Redirection après ajout

    return render(request, 'ajouter_categorie.html')


from django.shortcuts import render
from .models import ArticleDeBlog

from django.shortcuts import render, redirect
from .models import ArticleDeBlog, Profil, Panier

from django.shortcuts import render
from .models import ArticleDeBlog, Panier

def blog_posts(request):
    articles = ArticleDeBlog.objects.all().order_by('-date_creation')

    # Calculer le nombre d'articles dans le panier sans vérifier le profil
    nombre_produits_panier = Panier.objects.count()  # Compte tous les articles dans le panier

    return render(request, 'blog.html', {
        'articles': articles,
        'nombre_produits_panier': nombre_produits_panier,
    })

def propos(request):
    return render(request, 'propos.html')


from django.shortcuts import render, redirect
from .models import Pays
from django.contrib import messages

def ajouter_pays(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        code = request.POST.get('code')
        pays = Pays(nom=nom, code=code)
        pays.save()
        messages.success(request, 'Pays ajouté avec succès.')
        return redirect('admin_pannele')  # Redirection après ajout

    return render(request, 'ajouter_pays.html')



from django.shortcuts import render
from .models import Categorie, Produit

from django.shortcuts import render, get_object_or_404
from .models import Categorie, Produit, Profil, Panier
def produits_par_categorie(request):
    categories = Categorie.objects.all()
    produits_par_categorie = {}

    for categorie in categories:
        produits = Produit.objects.filter(categorie=categorie).order_by('-date_creation')
        produits_par_categorie[categorie] = produits

    # Compter le nombre d'articles dans le panier
    nombre_produits_panier = Panier.objects.count()  # Suppression de la vérification du profil

    context = {
        'produits_par_categorie': produits_par_categorie,
        'nombre_produits_panier': nombre_produits_panier,
    }

    return render(request, 'index.html', context)

from django.shortcuts import render, get_object_or_404
from .models import ArticleDeBlog

def blog_detail(request, article_id):
    article = get_object_or_404(ArticleDeBlog, id=article_id)
    return render(request, 'blog_detail.html', {'article': article})



# views.py
from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        whatsapp_number = request.POST.get('whatsapp_number')
        message = request.POST.get('message')

        # Enregistrer le message dans la base de données
        ContactMessage.objects.create(
            full_name=full_name,
            whatsapp_number=whatsapp_number,
            message=message
        )

        return redirect('produits_par_categorie')  # Redirection vers une page de succès ou d'accueil

    return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profil
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profil, Pays
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        numero_whatsapp = request.POST['whatsapp']
        pays_id = request.POST['pays']  # Ajout du pays
        password = request.POST['password']

        user = User.objects.create_user(username=numero_whatsapp, email=email, password=password)

        pays = Pays.objects.get(id=pays_id) if pays_id else None  # Recherche du pays sélectionné

        # Gestion de la photo
        photo = request.FILES.get('photo')

        profil = Profil.objects.create(
            user=user,
            nom=nom,
            prenom=prenom,
            email=email,
            numero_whatsapp=numero_whatsapp,
            pays=pays,
            photo=photo  # Ajout de la photo lors de la création du profil
        )

        login(request, user)
        return redirect('home')

    # Passer la liste des pays au template pour l'afficher dans le formulaire
    pays_list = Pays.objects.all()
    return render(request, 'signup.html', {'pays_list': pays_list})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        whatsapp = request.POST['whatsapp']
        password = request.POST['password']

        # Authentification de l'utilisateur
        user = authenticate(request, username=whatsapp, password=password)

        if user is not None:
            login(request, user)
            return redirect('afficher_profil')  # Remplacez 'home' par la route souhaitée après connexion
        else:
            messages.error(request, "Numéro WhatsApp ou mot de passe incorrect.")
            return render(request, 'signin.html')

    return render(request, 'signin.html')


from .models import Profil, Pays
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profil, Pays, Panier

def afficher_profil(request):
    # Vérification si l'utilisateur est connecté
    if not request.user.is_authenticated:
        return redirect('signin')

    try:
        profil = Profil.objects.get(user=request.user)
    except Profil.DoesNotExist:
        return redirect('signin')

    if request.method == 'POST':
        profil.nom = request.POST['nom']
        profil.prenom = request.POST['prenom']
        profil.email = request.POST['email']
        profil.numero_whatsapp = request.POST['numero_whatsapp']
        profil.pays_id = request.POST['pays']

        if 'photo' in request.FILES:
            profil.photo = request.FILES['photo']

        profil.save()

    # Calculer le nombre d'articles dans le panier
    if request.user.is_authenticated:
        try:
            profil = Profil.objects.get(user=request.user)
            nombre_produits_panier = Panier.objects.count()
        except Profil.DoesNotExist:
            nombre_produits_panier = 0
    else:
        nombre_produits_panier = 0

    pays_list = Pays.objects.all()
    return render(request, 'profil.html', {'profil': profil, 'pays_list': pays_list, 'nombre_produits_panier': nombre_produits_panier})



from django.shortcuts import render, get_object_or_404
from .models import Produit, Categorie

from django.shortcuts import render, get_object_or_404
from .models import Produit

def produit_detail(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produits_suggeres = Produit.objects.filter(categorie=produit.categorie).exclude(id=produit_id)[:4]

    return render(request, 'detail.html', {
        'produit': produit,
        'produits_suggeres': produits_suggeres
    })




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Avis, Profil

@login_required
def ajouter_avis(request):
    if request.method == 'POST':
        commentaire = request.POST.get('commentaire')
        note = request.POST.get('note')

        # Assurez-vous que la note est un nombre valide et dans la plage souhaitée
        try:
            note = int(note)
            if not (1 <= note <= 5):
                raise ValueError
        except (ValueError, TypeError):
            # Gérer les erreurs, par exemple, en redirigeant vers une page d'erreur ou en affichant un message d'erreur
            return redirect('home')  # Redirige vers la page d'accueil si l'entrée est invalide

        # Crée un nouvel avis
        profil = Profil.objects.get(user=request.user)
        avis = Avis(profil=profil, commentaire=commentaire, note=note)
        avis.save()

        return redirect('home')  # Redirige vers la page d'accueil après l'ajout

    return render(request, 'ajouter_avis.html')

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produit, Panier, Profil



from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produit, Panier, Profil

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Produit, Panier


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Produit, Panier

def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    # Vérifie si le produit est déjà dans le panier
    panier, created = Panier.objects.get_or_create(produit=produit)

    if not created:
        panier.quantite += 1
        panier.save()

    # Ajouter un message de confirmation
    messages.success(request, f"{produit.nom} a été ajouté à votre panier.")

    return redirect('produits_par_categorie')  # Redirige vers la page d'affichage des produits



from django.shortcuts import render
from .models import Panier
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Panier, Profil

from django.shortcuts import render, get_object_or_404
from .models import Produit, Panier, Profil


from django.shortcuts import render, redirect
from .models import Panier

def afficher_panier(request):
    # Récupérer tous les paniers
    paniers = Panier.objects.all()

    total_panier = 0  # Initialiser le total du panier
    produits_panier = []

    for panier in paniers:
        produit = panier.produit
        quantite = panier.quantite
        prix_unitaire = produit.prix_commercial
        total_produit = prix_unitaire * quantite  # Calculer le total pour ce produit
        total_panier += total_produit  # Ajouter au total du panier

        produits_panier.append({
            'produit': produit,
            'quantite': quantite,
            'prix_unitaire': prix_unitaire,
            'total_produit': total_produit,
        })

    context = {
        'produits_panier': produits_panier,
        'total_panier': total_panier,
    }

    return render(request, 'panier.html', context)




from django.shortcuts import redirect, get_object_or_404
from .models import Panier, Profil

from django.shortcuts import get_object_or_404, redirect
from .models import Panier

def supprimer_du_panier(request, produit_id):
    # Récupérer le panier avec le produit spécifique sans filtrer par profil
    panier = get_object_or_404(Panier, produit_id=produit_id)

    # Supprimer l'élément du panier
    panier.delete()

    # Rediriger vers la vue du panier
    return redirect('afficher_panier')



from django.shortcuts import render
from .models import Produit, ArticleDeBlog, Profil, Avis

def admin_pannele(request):
    produits = Produit.objects.all()
    articles = ArticleDeBlog.objects.all()
    profils = Profil.objects.all()
    avis = Avis.objects.all()

    context = {
        'produits': produits,
        'articles': articles,
        'profils': profils,
        'avis': avis,
    }

    return render(request, 'admin_pannele.html', context)







from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Produit, ArticleDeBlog
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Produit

def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == "POST":
        produit.delete()
        messages.success(request, f"Le produit '{produit.nom}' a été supprimé avec succès.")
        return redirect(reverse('admin_pannele'))  # Redirige vers 'admin_pannele' après suppression
    return redirect('admin_pannele')  # Si la requête n'est pas POST, on retourne à l'admin




from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import ArticleDeBlog

def supprimer_article_blog(request, article_id):
    article = get_object_or_404(ArticleDeBlog, id=article_id)
    if request.method == "POST":
        article.delete()
        messages.success(request, f"L'article '{article.titre}' a été supprimé avec succès.")
        return redirect(reverse('admin_pannele'))  # Redirige vers 'admin_pannele' après suppression
    return redirect('admin_pannele')  # Si la requête n'est pas POST, on retourne à l'admin
