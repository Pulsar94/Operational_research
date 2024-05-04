from Classtab import Tab
import os
import contextlib


def input_file():
    """
    Ask the user to choose a constraint table
    :return num_file: the number of the file to read
    """
    num_file = 0
    while num_file < 1 or num_file > 12:
        try:
            num_file = int(input("Veuillez choisir une table de contrainte de "
                                 "1 à 12 en inscrivant le numéro de la table : "))
            if num_file < 1 or num_file > 12:
                print("Veuillez entrer un numéro de table valide")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return num_file


def read_file(filename):
    """
    Read file, remove backslash n, and return a list of steps from the constraint table
    :param filename: the name of the file
    :return steps: a list of steps from the constraint table
    """
    with open(filename, 'r') as f:
        data = f.readlines()

        # removing backslash n from the end of the line
        for i in range(0, len(data)):
            data[i] = remove_backslashn(data[i])

        # splitting the line by comma
        steps = []
        for i in range(0, len(data)):
            steps.append(data[i].split(','))
            # splitting each steps by space
            steps[i] = steps[i][0].split(' ')
            # recursive function to remove empty string and counter out of range
            steps[i] = remove_empty_strings(steps[i])

    # converting the second element (weight) of each step to int
    for i in range(0, len(steps)):
        for j in range(0, len(steps[i])):
            steps[i][j] = int(steps[i][j])

    return steps


def remove_backslashn(step):
    """
    Remove backslash n from the end of line
    :param step: The line with a backslash n
    :return step: The line without backslash n
    """
    if step[-1] == "\n":
        step = step[:-1]
    return step


def remove_empty_strings(lst, index=0):
    """
    Remove empty strings from a list recursively to avoid out of range
    :param lst: The list to remove empty strings from
    :param index: The current index (default is 0)
    :return: The list without empty strings
    """
    if index == len(lst):
        return lst
    if lst[index] == '':
        lst.pop(index)
        return remove_empty_strings(lst, index)
    else:
        return remove_empty_strings(lst, index + 1)


def problem_initialization(num_file):
    """
    Initialize the problem with the constraint table
    :param num_file: number of the file to read
    :return problem_table: the problem table
    """
    # read file
    constraint_table = read_file("./constraint_tables/table_" + str(num_file) + ".txt")

    # initialize problem table
    tab_problem = Tab()

    # add cout to the problem table
    # len(constraint_table) - 1 to avoid the last line which is specific to command
    for i in range(0, len(constraint_table) - 1):
        temporary_list = []
        # len(constraint_table[i]) - 1 to avoid the last element which is specific to provider
        for j in range(0, len(constraint_table[i]) - 1):
            temporary_list.append(constraint_table[i][j])
        # append the temporary list of cost to the problem table cost section
        tab_problem.cout.append(temporary_list)

    # add command to the problem table
    # len(constraint_table[-1]) to get the last line which is the total of a specific command
    for i in range(0, len(constraint_table[-1])):
        tab_problem.command.append(constraint_table[-1][i])

    # add provider to the problem table
    # len(constraint_table) - 1 to avoid the last line (command) and get all the providers
    for i in range(0, len(constraint_table) - 1):
        tab_problem.provider.append(constraint_table[i][-1])

    return tab_problem


def traces_execution():
    """
    Test all the functions and write all the result in txt file
    :param: None
    """
    # Check if the directory contain all the test files : to know if the file traces.txt already exists
    # path of the directory
    path = "B2_traces_execution"
    # Check if the directory exists
    if not os.path.exists(path):
        os.makedirs(path)
    # Getting the list of directories
    dir_traces = os.listdir(path)
    # Checking if the list of directories contains all the test files
    if len(dir_traces) < 12:

        # Running the function for each file
        for num_file in range(1, 13):
            problem_table = problem_initialization(num_file)
            with open(f"B2_traces_execution/B2_trace{num_file}.txt", "w", encoding="utf-8") as f:
                f.write("----------- Etape 1 : Lecture & affichage de la table de contrainte -----------\n")
                # Number of providers
                f.write(f"Nombre de producteurs : {len(problem_table.provider)}\n")

                # Number of commands
                f.write(f"Nombre de commandes : {len(problem_table.command)}\n")

                f.write("\n-------------------- Etape 2 : Nord-Ouest --------------------\n")
                # Redirect the std output to the file
                with contextlib.redirect_stdout(f):
                    problem_table.nord_ouest()
                    problem_table.print_tab_traces()

                f.write("\n-------------------- Etape 3 : Balas-Hammer --------------------\n")
                # Redirect the std output to the file
                with contextlib.redirect_stdout(f):
                    problem_table.balas_hammer()
                    problem_table.print_tab_traces()
