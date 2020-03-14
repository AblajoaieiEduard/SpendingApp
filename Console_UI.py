'''
Created on Feb 7, 2020

@author: Eduard
'''
from Service import *
from Exceptions import *


class ConsoleUI():
    def __init__(self, serv1, serv2):
        self.__serv_cat = serv1
        self.__serv_chel = serv2
        self.__menu = "1.Adaugati categorie\n2.Stergeti o categorie\n3.Modificati o categorie\n4.Afisati situatia unei categorii\n5.Afisati situatia generala.\n6.Adauga o cheltuiala\n7. Sterge o cheltuiala.\n8.Modifica o cheltuiala\nx. Iesi din aplicatie"
    
    def show_menu(self):
        print(self.__menu)
    
    def add_cat(self):
        while True:
            nume = input("Da numele categoriei: ")
            while True:
                try:
                    buget = int(input("Cati bani vrei sa aloci acestei categorii?\nRaspuns: "))
                    break
                except ValueError:
                    print("Bugetul trebuie sa fie un numar intreg.")
            try:
                self.__serv_cat.adauga(nume, buget)
                break
            except RepoException as re:
                print(re)
            except CategorieException as ce:
                print(ce)
    
    def sub_cat(self):
        while True:
            nume = input("Dati numele categoriei de sters: ")
            try:
                self.__serv_cat.sterge(nume)
                break
            except RepoException as re:
                print(re)
            except CategorieException as ce:
                print(ce)
    
    def modify_cat(self):
        while True:
            nume = input("Dati numele categoriei de modificat: ")
            while True:
                try:
                    buget = int(input("Noul buget maxim pentru aceasta categorie: "))
                    break
                except ValueError:
                    print("Bugetul trebuie sa fie un numar intreg")
            try:
                self.__serv_cat.modifica(nume, buget)
                break
            except RepoException as re:
                print(re)
            except CategorieException as ce:
                print(ce)
    
    def category_sit(self):
        while True:
            nume = input("Dati numele categoriei pentru care vreti sa aflati situatia.")
            try:
                print(self.__serv_cat.situatie_categorie(nume))
                break
            except RepoException as re:
                print(re)
    
    def general(self):
        print(self.__serv_cat.situatie_generala())
    
    def add_chel(self):
        while True:
            while True:
                try:
                    suma = int(input("Ce suma ai cheltuit?\nRaspuns: "))
                    break
                except ValueError:
                    print("Suma trebuie sa fie un numar intreg")
            cat = input("Ce categorie?\nRaspuns:")
            desc = input("Ai o descriere?\nRaspuns: ")
            try:
                self.__serv_chel.adauga(suma, cat, desc)
                break
            except Exception as ex:
                print(ex)
    def __print_all_chel(self):
        print("Cheltuielile actuale sunt: ")
        print("ID  Zi  Luna     An   Suma Categoria   Descrierea")
        for chel in self.__serv_chel.get_all_chel():
            print(chel)
            
    def sub_chel(self):
        while True:
            self.__print_all_chel()
            while True:
                try:
                    id = int(input("Alege indicele cheltuielii pe care doresti sa o stergi.\nRaspuns:"))
                    break
                except ValueError:
                    print("ID trebuie sa fie un numar intreg")
            try:
                self.__serv_chel.sterge(id)
                break
            except RepoException as ex:
                print(ex)
            except ServiceException as ex:
                print(ex)
    def modify_chel(self):
        while True:
            self.__print_all_chel()
            while True:
                try:
                    id = int(input("Alege indicele cheltuielii pe care doresti sa o stergi.\nRaspuns:"))
                    break
                except ValueError:
                    print("ID trebuie sa fie un numar intreg")
            while True:
                try:
                    suma = int(input("Ce suma ai cheltuit?\nRaspuns: "))
                    break
                except ValueError:
                    print("Suma trebuie sa fie un numar intreg")
            cat = input("Ce categorie?\nRaspuns:")
            desc = input("Ai o descriere?\nRaspuns: ")
            try:
                self.__serv_chel.modifica(id, suma, cat, desc)
                break
            except Exception as ex:
                print(ex)