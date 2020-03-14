"""
Repo, clase pentru gestionat liste de categorii, cheltuieli
"""
from Exceptions import *
from Domain import *

class RepoGeneral():
    """
    Format general pentru clase de tip repo
    fisier = string, numele fisierului din care se preiau si se salveaza datele
    type = tipul obiectelor din multimea de obiecte
    lista = lista de obiecte de acelasi tip
    """
    def __init__(self, fisier, tip):
        self.__fisier = fisier
        self.__type = tip
        self.__lista = self._load_from_file()
    
    def get_all(self):
        self._load_from_file()
        return self.__lista[:]
    
    
    def size(self):
        return len(self.__lista)
    
    
    def save_to_file(self):
        """
        Salveaza in fisier configuratia actuala din lista
        """
        with open(self.__fisier, "w") as f:
            for el in self.__lista:
                atr = ';'.join(el.campuri())#fiecare clasa din domeniu are o functie campuri care returneaza o lista cu campurile clasei            
                f.write(atr.strip()) #strip se ocupa de spatii suplimentare
                f.write(';')
                f.write('\n')

                
    
    def _load_from_file(self):
        """
        Incarca din fisier configuratia actuala a listei
        """
        rez = []
        with open(self.__fisier,"r") as f:
            for line in f:
                if not line.isspace() and not line == '\n':
                    atr = line.split(';')
                    atr = atr[:-1] # scot /n de la final
                    rez.append(self.__type(*atr)) # type este clasa elementelor din repo. Poti transmite nume de clase ca parametri doamne ce cool :3
                    # *atr pune ca parametrii functiei elementele din lista atr
                    # sunt entuziasmat e foarte jmk
        return rez        
    def adauga(self, elem):
        """
        Adauga un element in lista daca nu a fost deja adaugat
        Raises: RepoException daca elementul a fost deja adaugat
        """
        self._load_from_file()
        if elem not in self.__lista:
            self.__lista.append(elem)
            self.save_to_file()
            return
        raise RepoException("Este deja adaugata.")
        
    def sterge(self, elem):
        """
        Sterge un element din lista
        raises: RepoException daca nu exista obiectul de sters in lista
        """
        self._load_from_file()
        if elem in self.__lista:
            self.__lista.remove(elem)
            self.save_to_file()
            return
        raise RepoException("Nu exista.")
    
    def cauta(self, elem):
        """
        Cauta un obiect in lista.Returneaza obiectul respectiv
        Raises RepoException daca nu il gaseste
        """
        self._load_from_file()
        if elem in self.__lista:
            i = self.__lista.index(elem)
            return self.__lista[i]
        raise RepoException("Nu exista.")
    
    def modifica(self, elem):
        """
        Modifica un element din lista
        Raises RepoException daca obiectul de modificat nu se afla in lista
        """
        self._load_from_file()
        if elem in self.__lista:
            i = self.__lista.index(elem)
            self.__lista[i] = elem
            self.save_to_file()
            return
        raise RepoException("Nu exista.")

class RepoCategorie(RepoGeneral):
    def __init__(self, fisier):
        RepoGeneral.__init__(self, fisier,Categorie)
    
    def get_total(self, fis):
        with open(fis, 'r') as f:
            x = f.readline()
        if x == '':
            return 0
        return float(x)
        
    def set_total(self, fis, total):
        with open(fis, 'w') as f:
            f.write(str(total))

class RepoCheltuiala(RepoGeneral):
    def __init__(self, fisier):
        RepoGeneral.__init__(self, fisier, Cheltuiala)

    def dec(self, cheltuiala):
        self._load_from_file()
        cheltuiala.dec()
        self.save_to_file()
    
    def get_counter(self, fis):
        with open(fis, 'r') as f:
            return int(f.read().strip())

    def set_counter(self, fis, counter):
        with open(fis, 'w') as f:
            f.write(str(counter))
            
