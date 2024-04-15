class Tab:
    def __init__(self):
        self.content = []#contenu du tableau --> 1 ligne 1 tableau en plus
        self.cout = [] #meme place que content cout de l'unité --> pour fictif cout négtifs
        self.command = [] #total des commandes par lignes [0]=total C1
        self.provider = [] #total des fournisseurs par colonnes [0]=total F1

        #ajouter des trucs si besoin

#faire les fonctions affiches --> tibitou
    def txt_to_tab(self): #tibitou
        #lire fichier txt
        pass


    def balas_hammer(self): #marc
        #Balas-Hammer
        if self.add_fictif()==False:
            print("No need to add fictif")
        else:
            print("Fictif have been added")
        #penalites
        choice_pen = self.penalites()
        if choice_pen[2] == 1:
            print("ligne", choice_pen[1], "avec une penalité de", choice_pen[0])
        else:
            print("colonne", choice_pen[1], "avec une penalité de", choice_pen[0])

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

    def copie_tab(self, tab):
        cop = []
        for lign in tab:
            cop.append(lign)
        return cop

    def penalites(self):
        #choix de si c'est une ligne ou une colonne à prendre et renvoie la valeur de la penalité et sa position
        #penalites comprenant les fictifs et les non fictifs pour les lignes

        #vérifier qu'il y a pas de soucis avec les fictifs
        max_row = -1
        pos_max_row = -1

        for i in range(len(self.cout)):
            for j in range(len(self.cout[i])):
                row = self.copie_tab(self.cout[i])
                row.sort()
                if row[0] == 0:
                    diff_row = row[2]-row[1]
                else:
                    diff_row = row[1]-row[0]
                if diff_row > max_row:
                    max_row = diff_row
                    pos_max_row = i

        max_col = -1
        pos_max_col = -1
        col = self.copie_tab(self.cout)
        temp_cout = zip(*col)
        pos_now=0
        for i in temp_cout:
            tab_col = list(i)
            tab_col.sort()
            #vérifier si l'ensemble des valeurs n'est pas des 0
            cpt = 0
            for nb_0 in tab_col:
                if nb_0 == 0:
                    cpt += 1
            if cpt != len(tab_col):#on ne prend pas en compte les rajout de sources fictives
                if tab_col[0] == 0:
                    diff_col = tab_col[2]-tab_col[1]
                else:
                    diff_col = tab_col[1]-tab_col[0]
                if diff_col > max_col:
                    max_col = diff_col
                    pos_max_col = pos_now
            pos_now += 1

        final_take = max(max_row, max_col)
        if final_take == max_row:
            return final_take, pos_max_row, 1 #1 if it's a row
        else:
            return final_take, pos_max_col, 2 #2 if it's a col







    def max_penalite(self):#4.2
        #max penalité --> ne pas prenre en compte les pénalités des fictifs
        pass

    def choix_to_fill(self):
        #choix pour remplir
        pass




    def nord_ouest(self): #quentin
        #nord ouest
        pass

    def is_acyclic(self): #quentin
        #acyclique avec parcour en largeur
        pass
    def is_connexe(self): #quentin
        #connexe
        pass



    def marche_pied(self):#tao
        #marche à pied
        pass

    def cout_potentiel(self):
        #cout potentiel
        pass

    def cout_marginaux(self):
        #cout marginaux
        pass


