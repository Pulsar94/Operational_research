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
        pass

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
    


    def is_connexe(self, virtual):
        node_count = len(self.provider) + len(self.command)
        edge_count = 0
        for i in range(len(self.provider)):
            for j in range(len(self.command)):
                if self.content[i][j] > 0 or (i,j) in virtual:
                    edge_count += 1
        
        return edge_count == node_count - 1
    
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
            virtual.append(add_fictif())

        return virtual
    
    def acquire_data_value(self, virtual):
        value_provider = {0:0}
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
    
        self.content[start_node[0]][start_node[1]] = debt
        for node in path:
            self.content[node[0]][node[1]] += -debt if negative else debt
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
            value_command, value_provider = self.acquire_data_value(virtual_links)
            potential_cost = self.cout_potentiel(value_command, value_provider)
            marginal_cost = self.cout_marginaux(potential_cost)
            loop = self.update_content(marginal_cost, virtual_links)
        print("content:", self.content)