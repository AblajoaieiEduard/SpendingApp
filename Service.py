'''
Created on Feb 3, 2020

@author: Eduard
'''
from Domain import *
from Validatori import *
from Repository import *
from datetime import *


class ServiceCategorie():
    """
    validator si repo stii ce sunt
    total alocat este o variabila intreaga in care se retine suma totala alocata pentru toate categoriile
    """
    def __init__(self, validator, repository, fis_total):
        self.__validator = validator
        self.__repo = repository
        self.__fis = fis_total
        self.__total_alocat = self.__repo.get_total(self.__fis)
    
    
    def get_total(self):
        return self.__total_alocat
    
    def size(self):
        return self.__repo.size()
    
    def get_all(self):
        return self.__repo.get_all()
    
    def adauga(self, nume, buget):
        """
        adauga o noua categorie
        raises categorieexception daca numele e vid sau bugetul <=0
                repoexception daca categoria deja exista
        """
        self.__total_alocat = self.__repo.get_total(self.__fis)
        categorie = Categorie(nume, buget, buget)
        self.__validator.valideaza(categorie)
        self.__repo.adauga(categorie)
        self.__total_alocat += buget
        self.__repo.set_total(self.__fis, self.__total_alocat)
    
    def sterge(self, nume):
        """
        sterge categoria cu numele dat
        raises repoexception daca nu exista categoria
        """
        self.__total_alocat = self.__repo.get_total(self.__fis)
        cat = self.__repo.cauta(Categorie(nume, 1, 1))
        self.__total_alocat -= cat.get_buget()
        self.__repo.sterge(Categorie(nume, 1, 1))
        self.__repo.set_total(self.__fis, self.__total_alocat)
        
    
    def modifica(self, nume, buget_nou):
        """
        modifica bugetul maxim pentru o anumita categorie
        """
        self.__total_alocat = self.__repo.get_total(self.__fis)
        cat = self.__repo.cauta(Categorie(nume, 1, 1))
        self.__total_alocat -= cat.get_buget()
        if buget_nou < cat.get_remanent():
            self.__repo.modifica(Categorie(nume,buget_nou, buget_nou))
        else:
            nou_remanent = buget_nou -  (cat.get_buget() - cat.get_remanent()) # din bugetul nou scad totalul cheltuit anterior 
            self.__repo.modifica(Categorie(nume, buget_nou, nou_remanent))
        self.__total_alocat += buget_nou
        self.__repo.set_total(self.__fis, self.__total_alocat)
    def situatie_categorie(self, nume):
        """
        primeste un nume de categorie
        returneaza un string de forma: buget ramas/buget maxim la acea categorie
        raises: RepoException daca nu exista categoria cautata
        """
        self.__total_alocat = self.__repo.get_total(self.__fis)
        cat = self.__repo.cauta(Categorie(nume, 1, 1))
        return str(cat.get_remanent()) + '/' + str(cat.get_buget())
    
    def situatie_generala(self):
        """
        returneaza un string de forma:
        buget ramas/ buget maxim
        """
        self.__total_alocat = self.__repo.get_total(self.__fis)
        bg = 0
        for cat in self.__repo.get_all():
            bg += cat.get_remanent()
        
        return str(bg) + '/' + str(self.__total_alocat)


class ServiceCheltuiala():
    """
    Se ocupa cu actiuni din viata reala asupra cheltuielilor.
    O sa faca cateva treburi cool
    """
    
    def __init__(self, validator, repo_cat, repo_chel, fis):
        self.__val = validator
        self.__categorii = repo_cat
        self.__cheltuieli = repo_chel
        self.__fis = fis
        ServiceCheltuiala.__count = self.__cheltuieli.get_counter(fis)
    
    def size_chel(self):
        return len(self.__cheltuieli.get_all())
    
    def get_all_chel(self):
        for chel in self.__cheltuieli.get_all():
            ok = 0
            for cat in self.__categorii.get_all():  
                if chel.get_categorie().lower() == cat.get_nume().lower():
                    ok = 1
                    break
            if ok == 0:
                self.__cheltuieli.sterge(chel)
                ServiceCheltuiala.__count -= 1
                self.__cheltuieli.set_counter(self.__fis, ServiceCheltuiala.__count)

        return self.__cheltuieli.get_all()
    
    def adauga(self, suma, categorie, descriere):
        """
        Functia se ocupa cu adaugarea unei cheltuieli
        in: suma cheltuita, categoria si descrierea
        Raises:
            ServiceException daca categoria nu exista
            CheltuialaException daca suma < 0 sau categoria e vida.
            RepoException daca deja exista cheltuiala respectiva
            
        """   
        x = datetime.now() # data curenta
        chel = Cheltuiala(ServiceCheltuiala.__count + 1, int(x.strftime("%d")), x.strftime("%B"), int(x.strftime("%Y")), suma, categorie, descriere )
        self.__val.valideaza(chel) # validez o posibila cheltuiala
        ok = 0
        for el in self.__categorii.get_all():
            if el.get_nume().lower() == categorie.lower():
                ok = 1
                break
        # ok = 1 -> categoria este valida
        if not ok:
            raise ServiceException("Invalid category.") # verific daca categoria exista
        cat = self.__categorii.cauta(Categorie(categorie, 1, 1))
        if cat.get_remanent() < suma:
            raise ServiceException("Budget is too small for this spending.")
        cat.cheltuie(suma) #cheltuiesc din bugetul ramas al categoriei
        ServiceCheltuiala.__count += 1 # numar ca am adaugat o cheltuiala
        self.__cheltuieli.adauga(chel)
        self.__categorii.save_to_file()
        self.__cheltuieli.set_counter(self.__fis, ServiceCheltuiala.__count)
        
    def sterge(self, id):
        """
        sterge o cheltuiala
        verifica daca id-ul exista
        """
        if id > ServiceCheltuiala.__count:
            raise ServiceException("Alege un Id valid.")
        chel = self.__cheltuieli.cauta(Cheltuiala(id, 1, "February", 2000, 1, "a", "b"))
        cat = self.__categorii.cauta(Categorie(chel.get_categorie(), 1, 1))
        cat.restituie(chel.get_suma())
        self.__categorii.save_to_file()
        self.__cheltuieli.sterge(chel)
        #am sters cheltuiala
        for cheltuiala in self.__cheltuieli.get_all():
            if cheltuiala.get_id() > id:
                self.__cheltuieli.dec(cheltuiala) # restabilesc lista cu Id-uri astfel incat sa fie numere consecutive
        ServiceCheltuiala.__count -= 1
        self.__cheltuieli.set_counter(self.__fis, ServiceCheltuiala.__count)
    
    def modifica(self, id, suma, categorie, descriere):
        if id > ServiceCheltuiala.__count:
            raise ServiceException("Alege un Id valid.")
        self.__val.valideaza(Cheltuiala(ServiceCheltuiala.__count + 1, 1, "Dec", 2000, suma, categorie, descriere))
        ok = 0
        for cat in self.__categorii.get_all():
            if cat.get_nume().lower() == categorie.lower():
                ok = 1
        if ok == 1:
            self.sterge(id)
            self.adauga(suma, categorie, descriere)
        else:
            raise ServiceException("Adauga mai intai categoria.")