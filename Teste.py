"""
Modul de teste unit
"""
import unittest
from Domain import *
from Validatori import *
from Repository import RepoGeneral, RepoCategorie, RepoCheltuiala
from Exceptions import RepoException, ValidationException
from Service import *

class Teste_Domeniu(unittest.TestCase):
    def testCategorie(self):
        categorie = Categorie("Mancare", 100, 100)
        self.assertTrue(categorie.get_nume() == "Mancare")
        self.assertTrue(categorie.get_buget() == 100)
        self.assertTrue(categorie.get_remanent() == 100)
    
    def testCheltuiala(self):
        cheltuiala = Cheltuiala(1, 25, "December", 2010, 50, "Mancare", "Croissant")
        self.assertTrue(cheltuiala.get_id() == 1)
        self.assertTrue(cheltuiala.get_zi() == 25)
        self.assertTrue(cheltuiala.get_luna() == "December")
        self.assertTrue(cheltuiala.get_an() == 2010)
        self.assertTrue(cheltuiala.get_suma() == 50)
        self.assertTrue(cheltuiala.get_categorie() == "Mancare")
        self.assertTrue(cheltuiala.get_descriere() == "Croissant")
    


class Teste_Validatori(unittest.TestCase):
    def setUp(self):
        self.validator_categorie = ValidatorCategorie()
        self.validator_cheltuiala = ValidatorCheltuiala()
    
    def testValideazaCategorie(self):
        with self.assertRaises(CategorieException):
            self.validator_categorie.valideaza(Categorie("", 7, 7))
        with self.assertRaises(CategorieException):
            self.validator_categorie.valideaza(Categorie("Mama",-5, -5))
        self.validator_categorie.valideaza(Categorie("Mama", 7, 7))
     
    def testValideazaCheltuiala(self):
        with self.assertRaises(CheltuialaException):
            self.validator_cheltuiala.valideaza(Cheltuiala(1,2, "December", 2010, 3,"","v"))
        with self.assertRaises(CheltuialaException):
            self.validator_cheltuiala.valideaza(Cheltuiala(1,2, "December", 2011, -5, "as", "vv"))
        self.validator_cheltuiala.valideaza(Cheltuiala(1,2, "December", 2010, 4, "as",""))
        

class Teste_Repo(unittest.TestCase):
    def setUp(self):
        self.repoCat = RepoCategorie("repo_categorie_test")
        self.repoChel = RepoCheltuiala("repo_cheltuiala_test")
        
    def tearDown(self):
        f = open("repo_categorie_test", 'w')
        f.close()
        f = open("repo_cheltuiala_test", 'w')
        f.close()
    
    def test_adauga_cat(self):
        self.assertTrue(self.repoCat.size() == 0)
        cat1 = Categorie("Mancare",1000, 1000)
        self.repoCat.adauga(cat1)
        self.assertTrue(self.repoCat.size() == 1)
        self.assertTrue(self.repoCat.get_all() == [cat1])
        cat2 = Categorie("Altele", 100, 100)
        self.repoCat.adauga(cat2)
        self.assertTrue(self.repoCat.size() == 2)
        self.assertTrue(self.repoCat.get_all() == [cat1, cat2])
        repoCat2 = RepoCategorie("repo_categorie_test")
        self.assertTrue( repoCat2.get_all() == self.repoCat.get_all())
        with self.assertRaises(RepoException):
            self.repoCat.adauga(Categorie("Mancare", 1000, 1000))
            
    def test_adauga_chel(self):
        self.assertTrue(self.repoChel.size() == 0)
        chel1 = Cheltuiala(1,2, "December", 2010, 3,"Mancare","Fubini")
        self.repoChel.adauga(chel1)
        self.assertTrue(self.repoChel.size() == 1)
        self.assertTrue(self.repoChel.get_all() == [chel1])
        chel2 = Cheltuiala(4,5,"December", 2010,6,"Altele", "Furau")
        self.repoChel.adauga(chel2)
        self.assertTrue(self.repoChel.size() == 2)
        self.assertTrue(self.repoChel.get_all() == [chel1, chel2])
        repoChel2 = RepoCheltuiala("repo_cheltuiala_test")
        self.assertTrue( repoChel2.get_all() == self.repoChel.get_all())
        with self.assertRaises(RepoException):
            self.repoChel.adauga(Cheltuiala(1,2,"December", 2010,3,"Mancare","Fubini"))
    
    def test_sterge_cat(self):
        cat1 = Categorie("Mancare",1000, 1000)
        cat2 = Categorie("Altele", 100, 100)
        cat3 = Categorie("Entertainment", 400, 400)
        cat4 = Categorie("Vin", 50, 50)
        self.repoCat.adauga(cat1)
        self.repoCat.adauga(cat2)
        self.repoCat.adauga(cat3)
        self.repoCat.adauga(cat4)
        self.repoCat.sterge(Categorie("Mancare",100, 100))
        self.assertTrue(self.repoCat.get_all() == [cat2, cat3, cat4])
        self.repoCat.sterge(Categorie("Entertainment",10, 10))
        self.assertTrue(self.repoCat.get_all() == [cat2, cat4])
        with self.assertRaises(RepoException):
            self.repoCat.sterge(Categorie("Cafea", 1, 1))
        repo2 = RepoCategorie("repo_categorie_test")
        assert repo2.get_all() == self.repoCat.get_all()
    
    def test_sterge_chel(self):
        chel1 = Cheltuiala(1,2,"December", 2010,3,"Mancare","buna")
        chel2 = Cheltuiala(2,3,"December", 2010,4,"Altele", "rau")
        chel3 = Cheltuiala(3,4,"December", 2010,5,"Vin","rosu")
        chel4 = Cheltuiala(4,5,"December", 2010,6,"Vin","alb")
        self.repoChel.adauga(chel1)
        self.repoChel.adauga(chel2)
        self.repoChel.adauga(chel3)
        self.repoChel.adauga(chel4)
        self.repoChel.sterge(Cheltuiala(1,2,"December", 2010,3,"Mancare","buna"))
        self.assertTrue(self.repoChel.get_all() == [chel2, chel3, chel4])
        self.repoChel.sterge(Cheltuiala(3,4,"December", 2010,5,"Vin","rosu"))
        self.assertTrue(self.repoChel.get_all() == [chel2, chel4])
        with self.assertRaises(RepoException):
            self.repoChel.sterge(Cheltuiala(5,6,"December", 2010,7,"cafea","jacobs"))
        repo2 = RepoCheltuiala("repo_cheltuiala_test")
        assert repo2.get_all() == self.repoChel.get_all()
    def test_cauta_cat(self):
        cat1 = Categorie("Mancare",1000, 1000)
        cat2 = Categorie("Altele", 100, 100)
        cat3 = Categorie("Entertainment", 400, 400)
        cat4 = Categorie("Vin", 50, 50)
        self.repoCat.adauga(cat1)
        self.repoCat.adauga(cat2)
        self.repoCat.adauga(cat3)
        self.repoCat.adauga(cat4)
        x = self.repoCat.cauta(Categorie("Entertainment", 1, 1))
        self.assertTrue(x == cat3)
        y = self.repoCat.cauta(Categorie("Vin", 1, 1))
        self.assertTrue(y == cat4)
        z = self.repoCat.cauta(Categorie("Entertainment", 2, 2))
        self.assertTrue(x == z)
        with self.assertRaises(RepoException):
            self.repoCat.cauta(Categorie("Dulciuri", 2, 2))
    
    def test_cauta_chel(self):
        chel1 = Cheltuiala(1,2,"December", 2010,3,"Mancare","buna")
        chel2 = Cheltuiala(2,3,"December", 2010,4,"Altele", "rau")
        chel3 = Cheltuiala(3,4,"December", 2010,5,"Vin","rosu")
        chel4 = Cheltuiala(4,5,"December", 2010,6,"Vin","alb")
        self.repoChel.adauga(chel1)
        self.repoChel.adauga(chel2)
        self.repoChel.adauga(chel3)
        self.repoChel.adauga(chel4)
        x = self.repoChel.cauta(Cheltuiala(3,4,"December", 2010,6,"Vinut","rosu"))
        self.assertTrue(x == chel3)
        y = self.repoChel.cauta(Cheltuiala(4,7,"December", 2010,6,"Vinut","alb"))
        self.assertTrue(y == chel4)
        z = self.repoChel.cauta(Cheltuiala(3,5,"December", 2010,6,"Vinut","rosu"))
        self.assertTrue(x == z)
        with self.assertRaises(RepoException):
            self.repoChel.cauta(Cheltuiala(8,9,"December", 2010,10,"mama","mea"))
            
        
    def test_modifica_cat(self):
        cat1 = Categorie("Mancare",1000, 1000)
        cat2 = Categorie("Altele", 100, 100)
        cat3 = Categorie("Entertainment", 400, 400)
        cat4 = Categorie("Vin", 50, 50)
        self.repoCat.adauga(cat1)
        self.repoCat.adauga(cat2)
        self.repoCat.adauga(cat3)
        self.repoCat.adauga(cat4)
        self.repoCat.modifica(Categorie("Mancare",500, 500))
        self.assertTrue(self.repoCat.cauta(cat1).get_buget() == 500)
        with self.assertRaises(RepoException):
            self.repoCat.modifica(Categorie("Gasca", 1, 1))
    
    def test_modifica_chel(self):
        chel1 = Cheltuiala(1,2,"December", 2010,3,"Mancare","buna")
        chel2 = Cheltuiala(2,3,"December", 2010,4,"Altele", "rau")
        chel3 = Cheltuiala(3,4,"December", 2010,5,"Vin","rosu")
        chel4 = Cheltuiala(4,5,"December", 2010,6,"Vin","alb")
        self.repoChel.adauga(chel1)
        self.repoChel.adauga(chel2)
        self.repoChel.adauga(chel3)
        self.repoChel.adauga(chel4)
        self.repoChel.modifica(Cheltuiala(1,20,"December", 2010,31,"Mancare","rea"))
        self.assertTrue(self.repoChel.cauta(chel1).get_zi() == 20)
        with self.assertRaises(RepoException):
            self.repoChel.modifica(Cheltuiala(5,6,"December", 2010,7,"Gasca","mare"))


class TestServiceCategorie(unittest.TestCase):
    def setUp(self):
        validator = ValidatorCategorie()
        repo = RepoCategorie("repo_categorie_test")
        self.serv = ServiceCategorie(validator, repo, "teste_total")
    
    def tearDown(self):
        f = open("repo_categorie_test",'w')
        f.close()
        f = open("teste_total", 'w')
        f.close()
    
    def test_adauga(self):
        self.assertTrue(self.serv.size() == 0)
        self.serv.adauga("Mancare", 100)
        self.assertTrue(self.serv.size() == 1)
        self.assertTrue(self.serv.get_all() == [Categorie("Mancare", 100, 100)])
        self.serv.adauga("Altele", 100)
        self.assertTrue(self.serv.size() == 2)
        self.assertTrue(self.serv.get_all() == [Categorie("Mancare", 100, 100), Categorie("Altele", 100, 100)])
        with self.assertRaises(ValidationException):
            self.serv.adauga("", 2)
        with self.assertRaises(RepoException):
            self.serv.adauga("Mancare", 50)
    
    
    def test_sterge(self):
        self.serv.adauga("Mancare", 100)
        self.serv.adauga("Altele", 1000)
        self.serv.adauga("Entertainment", 1010)
        self.serv.adauga("Cafea", 10)
        self.serv.sterge("Altele")
        self.serv.sterge("Mancare")
        self.assertTrue(self.serv.get_all() == [Categorie("Entertainment", 1010, 1010),Categorie("Cafea", 10, 10)])
    
    def test_modifica(self):
        self.serv.adauga("Mancare", 100)
        self.serv.adauga("Altele", 1000)
        self.serv.adauga("Entertainment", 1010)
        self.serv.adauga("Cafea", 10)
        self.serv.modifica("Mancare", 150)
        self.serv.modifica("Cafea", 100)
        self.assertTrue(self.serv.get_all() == [Categorie("Mancare", 150, 150), Categorie("Altele", 1000, 1000), Categorie("Entertainment", 1010, 1010),Categorie("Cafea", 100, 100)])
    
    def test_sit_cat(self):
        self.serv.adauga("Mancare", 100)
        self.serv.adauga("Altele", 1000)
        self.serv.adauga("Entertainment", 1010)
        self.serv.adauga("Cafea", 10)
        self.assertTrue(self.serv.situatie_categorie("Mancare") == "100/100")
    
    def test_sit(self):
        self.serv.adauga("Mancare", 100)
        self.serv.adauga("Altele", 1000)
        self.serv.adauga("Entertainment", 1010)
        self.serv.adauga("Cafea", 10)
        self.assertTrue(self.serv.situatie_generala() == "2120/2120")
        

class TestServiceCheltuiala(unittest.TestCase):
    def setUp(self):
        val = ValidatorCheltuiala()
        repo1 = RepoCategorie("repo_categorie_test")
        self.__cat1 = Categorie("Mancare",1000, 1000)
        cat2 = Categorie("Altele", 100, 100)
        cat3 = Categorie("Entertainment", 400, 400)
        cat4 = Categorie("Vin", 50, 50)
        repo1.adauga(self.__cat1)
        repo1.adauga(cat2)
        repo1.adauga(cat3)
        repo1.adauga(cat4)
        repo2 = RepoCheltuiala("repo_cheltuiala_test")
        f = open("test_counter", 'w')
        f.write("0")
        f.close()
        self.serv = ServiceCheltuiala(val, repo1, repo2, "test_counter")
        
    def tearDown(self):
        f = open("repo_categorie_test", 'w')
        f.close()
        f = open("repo_cheltuiala_test", 'w')
        f.close()
    
    def test_adauga(self):
        self.assertTrue(self.serv.size_chel() == 0)
        self.serv.adauga(100, "Mancare", "Place")
        self.assertTrue(self.serv.size_chel() == 1)
        self.assertTrue(self.serv.get_all_chel() == [Cheltuiala(1, int(datetime.now().strftime("%d")), datetime.now().strftime("%B"), int(datetime.now().strftime("%Y")), 100, "Mancare", "Place")])
        self.assertTrue(self.__cat1.get_remanent() == 900)
        self.serv.adauga(200, "Altele", "Place")
        self.assertTrue(self.serv.size_chel() == 2)
        self.assertTrue(self.serv.get_all_chel() == [Cheltuiala(1, int(datetime.now().strftime("%d")), datetime.now().strftime("%B"), int(datetime.now().strftime("%Y")), 100, "Mancare", "Place"), Cheltuiala(2, int(datetime.now().strftime("%d")), datetime.now().strftime("%B"), int(datetime.now().strftime("%Y")), 200, "Altele", "Place")])
        with self.assertRaises(ServiceException):
            self.serv.adauga(10, "Ceai", "Bun")
    
    def test_sterge(self):
        self.serv.adauga(100, "Mancare", "Place")
        self.serv.adauga(200, "Altele", "Place")
        with self.assertRaises(ServiceException):
            self.serv.sterge(3)
        self.serv.sterge(2)
        self.assertTrue(self.serv.get_all_chel() == [Cheltuiala(1, int(datetime.now().strftime("%d")), datetime.now().strftime("%B"), int(datetime.now().strftime("%Y")), 100, "Mancare", "Place")])
    
    def test_modifica(self):
        self.serv.adauga(100, "Mancare", "Place")
        self.serv.adauga(200, "Altele", "Place")
        with self.assertRaises(ServiceException):
            self.serv.modifica(3, 10, "A", "A")
        self.serv.modifica(2, 100, "Mancare", "meh")
        self.assertTrue(self.serv.get_all_chel() == [Cheltuiala(1, int(datetime.now().strftime("%d")), datetime.now().strftime("%B"), int(datetime.now().strftime("%Y")), 100, "Mancare", "Place") , Cheltuiala(2, int(datetime.now().strftime("%d")), datetime.now().strftime("%B"), int(datetime.now().strftime("%Y")), 100, "Mancare", "Meh")])
if __name__ == "__main__":
    unittest.main()