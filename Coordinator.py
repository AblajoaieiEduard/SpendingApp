'''
Created on Feb 7, 2020

@author: Eduard
'''
from Service import *
from Console_UI import *


def run():
    repo1 = RepoCategorie("categorii")
    repo2 = RepoCheltuiala("cheltuieli")
    val1 = ValidatorCategorie()
    val2 = ValidatorCheltuiala()
    serv1 = ServiceCategorie(val1, repo1, "total")
    serv2 = ServiceCheltuiala(val2, repo1, repo2, "counter")
    ui = ConsoleUI(serv1, serv2)
    while True:
        ui.show_menu()
        x = input("Da comanda: ")
        if x == '1':
            ui.add_cat()
        elif x == '2':
            ui.sub_cat()
        elif x == '3':
            ui.modify_cat()
        elif x == '4':
            ui.category_sit()
        elif x == '5':
            ui.general()
        elif x == '6':
            ui.add_chel()
        elif x == '7':
            ui.sub_chel()
        elif x == '8':
            ui.modify_chel()
        elif x == "x":
            break
        else:
            print("Comanda invalida.")
run()