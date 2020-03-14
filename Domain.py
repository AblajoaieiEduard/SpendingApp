"""
Modul o sa contina clase de obiecte care au un corespondent in lumea reala
categorie
cheltuiala
"""

class Categorie:
    """
    categorie - un tip de cheltuiala. Ex: mancare, entertainment
    are denumire si buget_maxim pe o saptamana
    """
    def __init__(self, nume, buget_maxim, buget_actual):
        nume = nume.lower()
        self.__nume = nume.capitalize()
        self.__buget_maxim = float(buget_maxim)
        self.__buget_actual = float(buget_actual)
    
    def get_nume(self):
        return self.__nume
    
    def get_buget(self):
        return self.__buget_maxim
    
    def get_remanent(self):
        return self.__buget_actual
    
    def cheltuie(self, suma):
        self.__buget_actual -= suma
    
    def restituie(self, suma):
        self.__buget_actual += suma
        
    def __eq__(self,other):
        return self.__nume.lower() == other.__nume.lower()
    
    def campuri(self):
        #returneaza o lista cu campurile unei categorii
        return [self.__nume,  str(self.__buget_maxim), str(self.__buget_actual)]
    
    def __str__(self):
        return self.__nume + '    ' + str(self.__buget_actual) + '/' + str(self.__buget_maxim)

class Cheltuiala:
    """cheltuiala - are ziua (sper eu generata automat), suma, categoria, descrierea
        are id pentru identificare unica
sper eu sa pot face lista de categorii setabila din meniu. categoria este o clasa, cheltuiala nu primeste un obiect, primeste denumirea
descrierea o sa fie optionala
    as vrea sa afiseze un mesaj cu scandal daca am trecut peste suma maxima stabilita
"""
    def __init__(self, id, zi, luna, an, suma, categorie, descriere):
        self.__id = int(id)
        self.__zi = zi
        self.__luna = luna
        self.__an = an
        self.__suma = float(suma)
        self.__categorie = categorie
        self.__descriere = descriere
    
    def dec(self):
        self.__id -= 1
        
    def get_id(self):
        return self.__id
    
    def get_zi(self):
        return self.__zi
    
    def get_luna(self):
        return self.__luna
    
    def get_an(self):
        return self.__an
    
    def get_suma(self):
        return self.__suma
    
    def get_categorie(self):
        return self.__categorie
     
    def get_descriere(self):
        return self.__descriere
    
    def __eq__(self,ot):
        return self.__id == ot.__id
    
    def campuri(self):
        #returneaza o lista cu campurile unei cheltuieli
        return [str(self.__id), str(self.__zi), self.__luna, str(self.__an), str(self.__suma), self.__categorie, self.__descriere]
    def __str__(self):
        return str(self.__id)+'.'+str(self.__zi) + ' ' + self.__luna + '  ' + str(self.__an) + '  ' + str(self.__suma) + '  ' + self.__categorie + '  ' + self.__descriere 


