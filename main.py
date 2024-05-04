from Classtab import Tab
from file import problem_initialization, input_file, traces_execution
import os
import time
from colorama import Fore, Style

# call the traces_execution function from file.py
traces_execution()


def load_problem_table():
    """
    Load the problem table
    :return problem_initialization(num_file): the problem table
    """
    os.system('cls')
    num_file = input_file()
    return problem_initialization(num_file)


def store_time(n, time1, time2, time3, time4, t):
    """
    Store the time in a file
    :param n: matrix size
    :param time1:
    :param time2:
    :param time3:
    :param time4:
    :param t:
    :return:
    """
    if not os.path.exists("time"):
        os.makedirs("time")

    with open("time/size_" + str(n) + "_t_" + str(t) + ".txt", "w") as f:
        f.write(f"Taille matrice : {n}\n")
        f.write(f"Temps execution algorithme Balas-Hammer : {time1}\n")
        f.write(f"Temps execution marche pied sur proposition de Balas-Hammer : {time2}\n")
        f.write(f"Temps execution algorithme Nord ouest : {time3}\n")
        f.write(f"Temps execution marche pied sur proposition de Nord ouest : {time4}\n")


def optimise_test():
    """
    Test the complexity of the algorithm
    :return:
    """
    start_time = time.time()
    t = 1

    try:
        n = int(input("Saisir la taille de la matrice carrée aléatoire à tester: "))
    except ValueError:
        print("Choix non valide. Veuillez réessayer.")

    time1, time2, time3, time4 = Tab().calculate_time(n)
    print("Complexité: ", n)
    print("Généré avec Nord ouest:", round(time3, 3), "seconds")
    print("Généré avec Balas-Hammer:", round(time1, 3), "seconds")
    print("Marche pied à partir de Balas-Hammer:", round(time2, 3), "seconds")
    print("Marche pied à partir de Nord-Ouest:", round(time4, 3), "seconds")
    store_time(n, time1, time2, time3, time4, t)


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

        try:
            choice = int(input("Saisissez votre choix : "))
        except ValueError:
            print("Choix non valide. Veuillez réessayer.")
            continue

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
        elif choice == 5:
            problem_table = load_problem_table()
        elif choice == 6:
            print("Sortie...")
            break
        else:
            print("Choix non valide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
