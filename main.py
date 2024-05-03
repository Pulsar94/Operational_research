from Classtab import Tab
from file import problem_initialization, input_file, traces_execution
import os
import time

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
        print("Complexity: ", n)
        print("Generating Nord_ouest:",round(time3,3), "seconds")
        print("Generating Balas:",round(time1,3), "seconds")
        print("Stepping Stone:",round(time2,3), "seconds")
        store_time(n, time1, time2, time3, t)
        n *= 2
        if n > 10000:
            store_time(999999999, time.time() - start_time, time.time() - start_time, time.time() - start_time, t)
            n = 2
            t += 1

def display_menu():
    print("\n--- Initialisation ---")

    print("Choisir une méthode d'initialisation")
    print("1. Initialisation avec Nord-Ouest")
    print("2. Initialisation avec Balas-Amer")
    print("3. Marche pied method")
    print("4. Marche pied with complexity calculation")
    print("5. Change constraint table")
    print("6. Exit")

def main():
    problem_table = load_problem_table()
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # Initialize with Nord-Ouest method
            problem_table.nord_ouest()
            problem_table.print_tab()
            print("Initialization done with Nord-Ouest method.")
        elif choice == 2:
            # Initialize with Balas-Amer method
            problem_table.balas_hammer()
            problem_table.print_tab()
            print("Initialization done with Balas-Amer method.")
        elif choice == 3:
            # Display table content
            if problem_table.content == []:
                print("Please initialize the table first!")
            else:
                problem_table.stepping_stone()
                problem_table.print_tab()
        elif choice == 4:
            # Marche pied with complexity calculation
            optimise_test()
        elif choice ==5 :
            problem_table = load_problem_table()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()