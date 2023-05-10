from .models import Produit,Fournisseur,Categorie
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm()
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list,'form':form})
def myProducts(request):
    products = Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context)

def nouveauFournisseur(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = FournisseurForm()
    list=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'list':list,'form':form}) 
@login_required
def home(request):
        context={'val':"Menu Acceuil"}
        return HttpResponseRedirect('/magasin')
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/registration.html',{'form' : form})

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,ProduitSerializer

class CategoryAPIView(APIView):
        def get(self, *args, **kwargs):
            categories = Categorie.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

class ProductAPIView(APIView):
        def get(self, *args, **kwargs):
            produits = Produit.objects.all()
            serializer = ProduitSerializer(produits, many=True)
            return Response(serializer.data)

from rest_framework import viewsets
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset