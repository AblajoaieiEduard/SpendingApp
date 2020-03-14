"""
Modul pentru validarea datelor.
"""
from Domain import Categorie,Cheltuiala
from Exceptions import CategorieException, CheltuialaException

class ValidatorCategorie:
    """
    clasa de validatori pentru obiecte de tip Categorie. Pot doar sa valideze
    """
    def valideaza(self, categorie):
        """
        numele nu are voie sa fie vid
        bugetul e mai mare ca 0
        raises CategorieException daca numele e vid sau bugetul <=0
        """
        if categorie.get_nume().isspace() or categorie.get_nume() == "\n" or categorie.get_nume() == "":
            raise CategorieException("Denumirea categoriei nu poate fi vida.")
        
        if categorie.get_buget() < 0:
            raise CategorieException("Bugetul pentru o categorie nu poate fi negativ.")
        
        
class ValidatorCheltuiala:
    def valideaza(self, cheltuiala):
        """
        id,zi generez automat, nu validez
        suma > 0
        categoria nevida
        descrierea poate fi vida.
        raises CheltuialaException daca cele de mai sus nu sunt indeplinite
        """
        if cheltuiala.get_suma() <= 0:
            raise CheltuialaException("Suma nu poate fi negativa sau nula.")
        if cheltuiala.get_categorie().isspace() or cheltuiala.get_categorie() == "\n" or cheltuiala.get_categorie() == "":
            raise CheltuialaException("Categoria nu poate fi vida.")
        
# trec adaugare cheltuiela prin ui si coord