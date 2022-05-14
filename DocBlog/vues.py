"""Fichier qui gére les vues d'une page html"""
from django.http import HttpResponse
from django.shortcuts import render

#Cette fonction retourne une template d'un fichier html.
def index_fonc(requets):
    """
      Cette fonction retourne un template html
    :param requets:
    :type requets:
    :return: une document html
    :rtype: de type template html
    """
    return render(requets, "DocBlog/index.html", context={"prenom": "Mamadou"})
