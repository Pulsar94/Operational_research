class Tab:
    def __init__(self):
        self.content = []#contenu du tableau --> 1 ligne 1 tableau en plus
        self.cout = [] #meme place que content cout de l'unité --> pour fictif cout négtifs
        self.command = [] #total des commandes par lignes [0]=total C1
        self.provider = [] #total des fournisseurs par colonnes [0]=total F1

        #ajouter des trucs si besoin

#faire les fonctions affiches --> tibitou
    def txt_to_tab(self): #tibitou
        "lire fichier txt"

    def total_command(self): #tibitou
        "calculer le total des commandes"

    def total_provider(self): #tibitou
        "calculer le total des fournisseurs"



    def balas_hammer(self): #marc
        #Balas-Hammer
        if self.add_fictif()==False:
            print("No need to add fictif")
        else:
            print("Fictif have been added")


    def is_command_equal_provider(self):#marc
        if sum(self.command) == sum(self.provider):
            return True#commande = fournisseur
        return False#commande != fournisseur


    def add_fictif(self): #marc
        #command/provider fictif
        if self.is_command_equal_provider()==True:
            return False#No need to add fictif

        if sum(self.command) < sum(self.provider):
            diff = sum(self.provider)-sum(self.command)
            self.command.append(diff)
            for i in range(len(self.cout)):
                self.cout[i].append(0)

        elif sum(self.command) > sum(self.provider):
            diff = sum(self.command)-sum(self.provider)
            self.provider.append(diff)
            self.cout.append([0]*len(self.cout[0]))
        return True#fictif have been added

    def penalites(self):
        #penalites

    def max_penalite(self):#4.2
        "max penalité --> ne pas prenre en compte les pénalités des fictifs"

    def choix_to_fill(self):
        "choix pour remplir"




    def nord_ouest(self): #quentin
        "nord ouest"

    def is_acyclic(self): #quentin
        "acyclique avec parcour en largeur"

    def is_connexe(self): #quentin
        "connexe"



    def marche_pied(self):#tao
        "marche à pied"

    def cout_potentiel(self):
        "cout potentiel"

    def cout_marginaux(self):
        "cout marginaux"


