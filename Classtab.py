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


    def add_fictif(self):
        #command/provider fictif
        if self.is_command_equal_provider()==True:
            return False#No need to add fictif

        if sum(self.provider) < sum(self.command):
            diff = sum(self.command)-sum(self.provider)
            self.provider.append(diff)
            self.cout.append([0] * len(self.cout[0]))


        elif sum(self.provider) > sum(self.command):
            diff = sum(self.provider)-sum(self.command)
            self.command.append(diff)

            for i in range(len(self.cout)):
                self.cout[i].append(0)
        return True#fictif have been added

    def copie_tab(self, tab):#obliger de créer une fonction de copie car sinon les valeurs sont liées et modifiées
        cop = []
        for lign in tab:
            cop.append(lign)
        return cop

    def penalites(self):
        max_row = -1
        pos_max_row = -1
        cpt_row = 0
        copie_cout = self.copie_tab(self.cout)
        for i in range(len(copie_cout)):
            for j in range(len(copie_cout[i])):
                if self.content[i][j] != -1:
                    copie_cout[i][j] = -1

        for i in range(len(copie_cout)):
            row = copie_cout[i]
            row = [nb for nb in row if nb != -1 and nb != 0]
            row.sort()

            if len(row) >= 2:
                diff_row = row[1] - row[0]
                if diff_row > max_row:
                    max_row = diff_row
                    pos_max_row = i
                if diff_row == max_row:#cas où il y a plusieurs pénalités identiques
                    res = self.choice_if_equals(pos_max_row, i, 0)
                    if res == 1:
                        max_row = diff_row
                        pos_max_row = i
            else:
                cpt_row += 1

        col_cout_transp = zip(*copie_cout)  # transposer le tableau pour avoir les colonnes sur les lignes plus facile à traiter
        col = list(col_cout_transp)  # transformation de la grande liste en un tableau
        for sous_tab in range(len(col)):  # finalisation de préparation en un tableau de 2dim
            col[sous_tab] = list(col[sous_tab])

        cpt_col = 0
        max_col = -1
        pos_max_col = -1

        for i in range(len(col)):
            col_ = [nb for nb in col[i] if nb != -1 and nb != 0]
            col_.sort()

            if len(col_) >= 2:
                diff = col_[1] - col_[0]
                if diff > max_col:
                    max_col = diff
                    pos_max_col = i
                if diff == max_col:#cas où il y a plusieurs pénalités identiques
                    res = self.choice_if_equals(pos_max_col, i, 1)
                    if res == 1:
                        max_col = diff
                        pos_max_col = i
            else:
                cpt_col += 1

        if cpt_col == len(col) and cpt_row == len(copie_cout):
            return -1, -1, -1

        if max_row == max_col:  # cas où les deux max pénalités sont identiques
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
            return final_take, pos_max_row, 1  # 1 if it's a row
        else:
            return final_take, pos_max_col, 2  # 2 if it's a col




    def choice_if_equals(self, pos, pos_diff, choice=None):#fct pour faire le choix entre deux lignes pour savoir laquelle choisir
        #prendre celui où plus grande quantité possible
        #choice=0 --> cas ligne
        #choice=1 --> cas colonne
        #choice=3 --> cas combiné
        if choice == 0:
            prv_max = self.provider[pos]
            prv_diff = self.provider[pos_diff]
            if prv_diff >= prv_max:
                return 1
            else:
                return 0

        if choice == 1:
            cmd_max = self.command[pos]
            cmd_diff = self.command[pos_diff]
            if cmd_diff >= cmd_max:
                return 1
            else:
                return 0

        if choice == 3:
            final_row = self.provider[pos]
            final_col = self.command[pos_diff]
            if final_row >= final_col:
                return 0
            else:
                return 1


    def find_pos(self, x=-1, y=-1):#trouve le plus petit en fonction de la ligne ou de la colonne
        if y == -1:
            if self.content[x][0] != -1:
                for nb in self.cout[x]:
                    if nb != -1:
                        min = nb
                        pos = self.cout[x].index(nb)
            else:
                min = self.cout[x][0]
                pos = 0
            for i in range(len(self.cout[x])):
                if self.content[x][i] == -1 and self.cout[x][i] < min and self.cout[x][i] != 0:
                    min = self.cout[x][i]
                    pos = i
            return x, pos

        else:#quand x = -1
            if self.content[0][y] != -1:
                for nb in self.cout:
                    if nb[y] != -1:
                        min = nb[y]
                        pos = self.cout.index(nb)
            else:
                min = self.cout[0][y]
                pos = 0
            for i in range(len(self.cout)):
                if self.content[i][y] == -1 and self.cout[i][y] < min and self.cout[i][y] != 0:
                    min = self.cout[i][y]
                    pos = i
            return pos, y

    def fill_BH(self, x, y):
        if self.provider[x] < self.command[y]:
            for i in range(len(self.cout[x])):
                if self.content[x][i] == -1:#Exclu les valeurs déjà remplies
                    self.content[x][i] = 0
            self.content[x][y] = self.provider[x]

            self.command[y] -= self.provider[x]
            return
        else:
            for i in range(len(self.cout)):
                if self.content[i][y] == -1:
                    self.content[i][y] = 0
            self.content[x][y] = self.command[y]
            self.provider[x] -= self.command[y]
            return

    def end_fill(self):
        to_add = 0
        for i in range(len(self.content)):
            for j in range(len(self.content[0])):
                if self.content[i][j] != -1:
                    to_add += self.content[i][j]
                else:
                    x = i
                    y = j
            if to_add <= self.provider[x]:
                self.content[x][y] = self.provider[x] - to_add
            to_add = 0


    def balas_hammer(self): #marc
        #savoir si il faut des fictifs
        if self.add_fictif()==False:
            print("No need to add fictif")
        else:
            print("Fictif have been added")

        #copie de provider et command et cout
        cout_before = []
        cou_sous_before = []
        for i in self.cout:
            for j in i:
                cou_sous_before.append(j)
            cout_before.append(cou_sous_before)
            cou_sous_before = []
        provider_before = self.copie_tab(self.provider)
        command_before = self.copie_tab(self.command)

        #init -1 self.content
        self.content = [[-1] * len(self.cout[0]) for _ in range(len(self.cout))]

        while (self.penalites()!=(-1, -1, -1)):
            #penalites
            choice_pen = self.penalites()

            #remplissage
            if choice_pen[2] == 1:
                print("ligne", choice_pen[1], "avec une penalité de", choice_pen[0])
                nb_to_fill = self.find_pos(choice_pen[1])#obtention de x et y du nombre à fill
                print("cout le plus bas à remplir ", self.cout[nb_to_fill[0]][nb_to_fill[1]], "x", nb_to_fill[0], "y", nb_to_fill[1])
                self.fill_BH(nb_to_fill[0], nb_to_fill[1])

            else:
                print("colonne", choice_pen[1], "avec une penalité de", choice_pen[0])
                nb_to_fill = self.find_pos(-1, choice_pen[1])
                print("cout le plus bas à remplir ", self.cout[nb_to_fill[0]][nb_to_fill[1]], "x", nb_to_fill[0], "y", nb_to_fill[1])
                self.fill_BH(nb_to_fill[0], nb_to_fill[1])
            print("cout", self.cout)
            print("content", self.content)
            print("command", self.command)
            print("provider", self.provider)
            print("\n")

        self.command = command_before
        self.provider = provider_before
        self.cout = cout_before

        self.end_fill()#remplissage des cases vides

        print("\n")
        print("cout", self.cout)
        print("content", self.content)
        print("command", self.command)
        print("provider", self.provider)
        print("\n")



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


