from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Blog/index.html", context={"prenom": "Mamadou"})
def articles(request, numero_article):
    print("L'article numéro", numero_article)
    return render(request, f"Blog/article-{numero_article}.html")
