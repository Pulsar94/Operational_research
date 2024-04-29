import random
import time

class Tab:
    def __init__(self):
        self.content = []#contenu du tableau --> 1 ligne 1 tableau en plus
        self.cout = [] #meme place que content cout de l'unité --> pour fictif cout négtifs
        self.command = [] #total des commandes par lignes [0]=total C1
        self.provider = [] #total des fournisseurs par colonnes [0]=total F1

        #ajouter des trucs si besoin

    def rand_fill(self, n):#remplissage aléatoire
        totalValue = n + random.randint(100, 10000)
        commandDebt = totalValue
        providerDebt = totalValue

        for i in range(n):
            self.cout.append([0] * n)
            self.content.append([-1] * n)
            if i == n-1:
                self.provider.append(providerDebt)
                self.command.append(commandDebt)
            else:
                self.command.append(random.randint(1, int(commandDebt/(n-i-1))))
                self.provider.append(random.randint(1, int(providerDebt/(n-i-1))))
                commandDebt -= self.command[i]
                providerDebt -= self.provider[i]
            for j in range(n):
                self.cout[i][j] = random.randint(1, 100)
    
    def calculate_time(self, n):
        starting_time = time.time()
        self.rand_fill(n)
        temp_command = self.command.copy()
        temp_provider = self.provider.copy()
        self.nord_ouest()
        nord_time = time.time() - starting_time

        starting_time = time.time()
        self.command = temp_command
        self.provider = temp_provider
        self.balas_hammer()
        balas_time = time.time() - starting_time
        self.stepping_stone()
        stepping_time = time.time() - starting_time - balas_time
        return balas_time, stepping_time, nord_time

    def show_tab(self):
        print("\t\t\t", end = "")
        for i in range(len(self.command)):
            print("C"+str(i), end="\t\t\t")
        print("SL\n")
        
        for i in range(len(self.provider)):
            print("\nS"+str(i), end="\t\t\t")
            for j in range(len(self.command)):
                print(str(self.content[i][j])+ " (" + str(self.cout[i][j])+")", end="\t\t\t")

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
        x = -1
        y = -1
        for i in range(len(self.content)):
            for j in range(len(self.content[0])):
                if self.content[i][j] == -1:
                    for nb in range(len(self.cout[i])):
                        if self.content[i][nb] != -1:
                            to_add += self.content[i][nb]
                        else:
                            x = i
                            y = nb
                    if x != -1 and y != -1:
                        self.content[x][y] = self.provider[x] - to_add
                    to_add = 0
                    x = -1
                    y = -1
        return


    def nord_ouest(self):
        command_temp = self.command
        provider_temp = self.provider
        if sum(command_temp) > sum(provider_temp) : 
            provider_temp.append(sum(command_temp)-sum(provider_temp))

        if sum(command_temp) < sum(provider_temp) : 
            command_temp.append(sum(provider_temp)-sum(command_temp))

        providersize = len(provider_temp)
        commandsize = len(command_temp)
        for i in range(providersize):
            self.content.append([0] * commandsize)
        
        cpt_provider = 0
        cpt_command = 0

        while cpt_provider < providersize and cpt_command < commandsize:
            if provider_temp[cpt_provider] < command_temp[cpt_command]:
                self.content[cpt_provider][cpt_command] = provider_temp[cpt_provider]
                command_temp[cpt_command] -= self.content[cpt_provider][cpt_command]
                cpt_provider += 1
            elif provider_temp[cpt_provider] > command_temp[cpt_command]:
                self.content[cpt_provider][cpt_command] = command_temp[cpt_command]
                provider_temp[cpt_provider] -= self.content[cpt_provider][cpt_command]
                cpt_command += 1
            else:  
                self.content[cpt_provider][cpt_command] = command_temp[cpt_command]
                cpt_provider += 1
                cpt_command += 1
        
        for i in range(len(self.content)):
            for j in range(len(self.content[0])):
                if self.content[i][j] == -1:
                    self.content[i][j] = 0
        return

    def balas_hammer(self): #marc
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
                #print("ligne", choice_pen[1], "avec une penalité de", choice_pen[0])
                nb_to_fill = self.find_pos(choice_pen[1])#obtention de x et y du nombre à fill
                #print("cout le plus bas à remplir ", self.cout[nb_to_fill[0]][nb_to_fill[1]], "x", nb_to_fill[0], "y", nb_to_fill[1])
                self.fill_BH(nb_to_fill[0], nb_to_fill[1])
            else:
                #print("colonne", choice_pen[1], "avec une penalité de", choice_pen[0])
                nb_to_fill = self.find_pos(-1, choice_pen[1])
                #print("cout le plus bas à remplir ", self.cout[nb_to_fill[0]][nb_to_fill[1]], "x", nb_to_fill[0], "y", nb_to_fill[1])
                self.fill_BH(nb_to_fill[0], nb_to_fill[1])
            #print("cout", self.cout)
            #print("content", self.content)
            #print("command", self.command)
            #print("provider", self.provider)
            #print("\n")

        self.command = command_before
        self.provider = provider_before
        self.cout = cout_before

        self.end_fill()#remplissage des cases vides

        #print("\n")
        #print("cout", self.cout)
        #print("content", self.content)
        #print("command", self.command)
        #print("provider", self.provider)
        #print("balas done\n")

    def is_acyclic(self): #quentin
        #acyclique avec parcour en largeur
        pass
    
    def is_connexe(self, virtual):
        node_count = len(self.provider) + len(self.command)
        edge_count = 0
        for i in range(len(self.provider)):
            for j in range(len(self.command)):
                if self.content[i][j] > 0 or (i,j) in virtual:
                    edge_count += 1
        return edge_count >= node_count - 1
    
    def set_connexe(self):
        virtual = []
        def add_fictif():
            node, cost = (0,0), self.cout[0][0]
            for i in range(len(self.provider)):
                for j in range(len(self.command)):
                    if self.content[i][j] == 0 and self.cout[i][j] < cost:
                        node, cost = (i,j), self.cout[i][j]
            return node

        while not self.is_connexe(virtual):
            if add_fictif() in virtual:
                return False
            virtual.append(add_fictif())

        return virtual
    
    def acquire_data_value(self, virtual):
        value_provider = {0:0}
        value_provider_copy = {0:0}
        value_command = {}

        def set_value(i,j):

            if i in value_provider:
                value_command[j] = value_provider[i] - self.cout[i][j]
                return False
            
            if j in value_command:
                value_provider[i] = self.cout[i][j] + value_command[j]
                return False

            return True
        
        loop = True
        while loop: # Lazy failsafe
            loop = False
            for i in range(len(self.provider)):
                for j in range(len(self.command)):
                    if ((i,j) in virtual or self.content[i][j] > 0) and set_value(i,j):
                        loop = True
            if value_provider_copy == value_provider:
                return False, False
            value_provider_copy = value_provider.copy()
        
        return value_command, value_provider
                    
    def cout_potentiel(self, value_command, value_provider):
        table = []
        for i in range(len(self.provider)):
            table.append([])
            for j in range(len(self.command)):
                table[i].append(value_provider[i] - value_command[j])
        return table

    def cout_marginaux(self, potential_cost):
        table = []
        for i in range(len(self.provider)):
            table.append([])
            for j in range(len(self.command)):
                table[i].append(self.cout[i][j] - potential_cost[i][j])
        return table
    
    def update_from_path(self, path):
        start_node = path.pop(0)
        path.pop(-1)
        debt = self.content[path[-1][0]][path[-1][1]]
        negative = True

        if debt <= 0:
            return False
    
        self.content[start_node[0]][start_node[1]] = debt
        for node in path:
            self.content[node[0]][node[1]] += -debt if negative else debt
            if self.content[node[0]][node[1]] < 0:
                debt += self.content[node[0]][node[1]]
                self.content[node[0]][node[1]] = 0
            negative = not negative

    def get_cyclic_path(self, new_node, virtual):
        virtual.append(new_node)

        def n_node(nodeList, command = False, first = False):
            node = nodeList[-1]

            if not first and node == new_node:
                return nodeList

            if not command:
                for i in range(len(self.provider)):
                    copy_list = nodeList.copy()
                    if i != node[0] and (self.content[i][node[1]] > 0 or (i,node[1]) in virtual):
                        copy_list.append((i,node[1]))
                        att = n_node(copy_list, True)
                        if att:
                            return att
            else:
                for j in range(len(self.command)):
                    copy_list = nodeList.copy()
                    if j != node[1] and (self.content[node[0]][j] > 0 or (node[0],j) in virtual):
                        copy_list.append((node[0],j))
                        att = n_node(copy_list, False)
                        if att:
                            return att            

        return n_node([new_node], False, True)

    def update_content(self, marginal_cost, virtual_links):
        node, cost = (0,0), marginal_cost[0][0]
        for i in range(len(self.provider)):
            for j in range(len(self.command)):
                if marginal_cost[i][j] < cost:
                    node, cost = (i,j), marginal_cost[i][j]
        
        if cost < 0:
            path = self.get_cyclic_path(node, virtual_links)
            self.update_from_path(path)
            return True
        
        return False

    def stepping_stone(self):
        loop = True
        while loop:
            virtual_links = self.set_connexe()
            if virtual_links == False:
                break
            value_command, value_provider = self.acquire_data_value(virtual_links)
            if value_command == False:
                break
            potential_cost = self.cout_potentiel(value_command, value_provider)
            marginal_cost = self.cout_marginaux(potential_cost)
            loop = self.update_content(marginal_cost, virtual_links)
        
        return True