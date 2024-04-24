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

    def copie_tab(self, tab):#obliger de créer une fonction de copie car sinon les valeurs sont liées et modifiées
        cop = []
        for lign in tab:
            cop.append(lign)
        return cop

    def penalites(self, done_row=[], done_col=[]):#done_row et done_col pos des truc deja remplis
        #choix de si c'est une ligne ou une colonne à prendre et renvoie la valeur de la penalité et sa position
        #penalites comprenant les fictifs et les non fictifs pour les lignes

        max_row = -1
        pos_max_row = -1
        for i in range(len(self.cout)):  # choix de la ligne max de penalité
            if i not in done_row:
                row = self.copie_tab(self.cout[i])
                row.sort()

                if row[0] == 0:
                    diff_row = row[2] - row[1]
                else:
                    diff_row = row[1] - row[0]

                if diff_row == max_row:#cas où il y a plusieurs pénalités identiques
                    res = self.choice_if_equals(pos_max_row, i, 0)
                    if res == 1:
                        max_row = diff_row
                        pos_max_row = i

                if diff_row > max_row:
                    max_row = diff_row
                    pos_max_row = i

        #choix de la colonne max en fonction de la pénalité
        max_col = -1
        pos_max_col = -1
        cop = self.copie_tab(self.cout)
        col_cout_transp = zip(*cop)#transposer le tableau pour avoir les colonnes sur les lignes plus facile à traiter
        col_cout_transp= list(col_cout_transp)#transformation de la grande liste en un tableau
        for sous_tab in range(len(col_cout_transp)):#finalisation de préparation en un tableau de 2dim
            col_cout_transp[sous_tab] = list(col_cout_transp[sous_tab])

        for i in range(len(col_cout_transp)):#même principe que les lignes mais sur le tableau modifié des colonnes
            if i not in done_col:
                col_cout_transp[i].sort()

                if col_cout_transp[i][0] == 0:
                    diff_col = col_cout_transp[i][2] - col_cout_transp[i][1]
                else:
                    diff_col = col_cout_transp[i][1] - col_cout_transp[i][0]

                if diff_col == max_col:#cas où il y a plusieurs pénalités identiques
                    res = self.choice_if_equals(pos_max_col, i, 1)
                    if res == 1:
                        max_col = diff_col
                        pos_max_col = i

                if diff_col > max_col:
                    max_col = diff_col
                    pos_max_col = i

        #choix final entre la row te la col
        if max_row == max_col : #cas où les deux max pénalités sont identiques
            res = self.choice_if_equals(pos_max_row, pos_max_col, 3)
            if res == 0:
                final_take = max_row
                return final_take, pos_max_row, 1  # 1 if it's a row
            else:
                final_take = max_col
                return final_take, pos_max_col, 2  # 2 if it's a col

        else:
            final_take = max(max_row, max_col)
        if final_take == max_row:
            return final_take, pos_max_row, 1 #1 if it's a row
        else:
            return final_take, pos_max_col, 2 #2 if it's a col

    def choice_if_equals(self, pos, pos_diff, choice=None):#fct pour faire le choix entre deux lignes pour savoir laquelle choisir
        #prendre celui où plus grande quantité possible
        #choice=0 --> cas colonne
        #choice=1 --> cas ligne
        #choice=3 --> cas combiné
        if choice == 0:
            cmd_max = self.command[pos]
            cmd_diff = self.command[pos_diff]
            if cmd_diff >= cmd_max:
                return 1
            else:
                return 0

        if choice == 1:
            prv_max = self.provider[pos]
            prv_diff = self.provider[pos_diff]
            if prv_diff >= prv_max:
                return 1
            else:
                return 0

        if choice == 3:
            final_row = self.command[pos]
            final_col = self.provider[pos_diff]
            if final_row >= final_col:
                return 0
            else:
                return 1

    def fill_with_penalitie_row(self, pos):
        temp_max = self.cout[pos][0]
        choix = 0
        for i in range(len(self.cout[pos])):  # TODO cas où il y a 2 couts identiques
            if self.cout[pos][i] < temp_max:
                temp_max = self.cout[pos][i]


    def fill_with_penalitie_col(self, pos):
        pass

    def balas_hammer(self): #marc
        #savoir si il faut des fictifs
        if self.add_fictif()==False:
            print("No need to add fictif")
        else:
            print("Fictif have been added")

        #penalites
        choice_pen = self.penalites()

        #remplissage
        if choice_pen[2] == 1:
            print("ligne", choice_pen[1], "avec une penalité de", choice_pen[0])
            self.fill_with_penalitie_row(choice_pen[1])

        if choice_pen[2] == 2:
            print("colonne", choice_pen[1], "avec une penalité de", choice_pen[0])
            self.fill_with_penalitie_col(choice_pen[1])
        #faire remplir le plus petit continuer et faire des copies et tout




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


