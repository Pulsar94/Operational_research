from Classtab import Tab
from file import problem_initialization, input_file, traces_execution
import os
import time
from colorama import Fore, Style

# ------------------------- Reading file and start of the program -------------------------
traces_execution()
def load_problem_table():
    os.system('cls')
    num_file = input_file()
    return problem_initialization(num_file)



def store_time(n, time1, time2, time3, t):
    if not os.path.exists("time"):
        os.makedirs("time")

    with open("time/size_"+str(n)+"_t_"+str(t)+".txt", "w") as f:
        f.write(str(n) + "\n" + str(time1) + "\n" + str(time2) + "\n" + str(time3))


def optimise_test():
    start_time = time.time()
    n = 4
    t = 1
    while True:
        time1, time2, time3 = Tab().calculate_time(n)
        print("Complexité: ", n)
        print("Généré avec Nord ouest:",round(time3,3), "seconds")
        print("Généré avec Balas-Hammer:",round(time1,3), "seconds")
        print("Marche pied:",round(time2,3), "seconds")
        store_time(n, time1, time2, time3, t)
        n *= 2
        if n > 10000:
            store_time(999999999, time.time() - start_time, time.time() - start_time, time.time() - start_time, t)
            n = 2
            t += 1

def display_menu():
    print("\n--- MENU ---")
    print("1. Initialisation avec Nord-Ouest")
    print("2. Initialisation avec Balas-Hammer")
    print("3. Méthode du marche pied")
    print("4. Marche pied avec calcul de la complexité")
    print("5. Changer la table des contraintes")
    print("6. Quitter")

def main():
    problem_table = load_problem_table()
    while True:
        display_menu()
        choice = int(input("Saisissez votre choix : "))
        if choice == 1:
            problem_table.nord_ouest()
            problem_table.print_tab()
            print(f"Initialisation par la méthode Nord-Ouest : Flot({Fore.RED}coût{Style.RESET_ALL})")
        elif choice == 2:
            problem_table.balas_hammer()
            problem_table.print_tab()
            print(f"Initialisation par la méthode Balas-Hammer : Flot({Fore.RED}coût{Style.RESET_ALL})")
        elif choice == 3:
            if problem_table.content == []:
                print("Veuillez d'abord initialiser le tableau!")
            else:
                problem_table.stepping_stone()
                problem_table.print_tab()
        elif choice == 4:
            optimise_test()
        elif choice ==5 :
            problem_table = load_problem_table()
        elif choice == 6:
            print("Sortie...")
            break
        else:
            print("Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()