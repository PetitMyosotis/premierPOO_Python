# Définition de la classe Personne
class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.majeur = None
        self.nom = nom # création d'une varibale d'instance
        self.age = age
        print(f"Constructeur personne: {nom} {age}")

    def EstMajeur(self):  # déclare une nouvelle méthode d'instance
        if self.age >= 18:
            return True
        return False

    '''peut aussi s'écrire:
    def EstMajeur(self):
        return self.age >=18'''

    def DemanderNom(self):
        self.nom = input("Entrez votre nom s'il vous plait")

    def SePresenter(self): # déclare une méthode d'instance
        if self.nom == "":
            self.DemanderNom()
        print(f"Bonjour, je m'appelle {self.nom}", end=" ")
        if self.age > 0:
            print(f" j'ai {self.age} ans et", end=" ")
            if self.EstMajeur():
                print("je suis majeur")
            else:
                print("je suis mineur")



#Utilisation de la classe Personne

personne1 = Personne("Jean", 30) # création d'une instance de Personne
personne2 = Personne("Paul", 15) # création d'une nouvelle instance de Personne
personne3 = Personne() # création d'une nouvelle instance de Personne
personne1.SePresenter() # appel la methode SePresenter sur l'objet personne1 de type Personne
personne2.SePresenter() # appel la méthode SePresenter sur l'objet personne2 de type Personne
personne3.SePresenter() # appel la méthode SePresenter sur l'objet personne2 de type Personne

