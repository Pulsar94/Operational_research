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
        num_file = int(input("Veuillez choisir une table de contrainte de "
                             "1 à 14 en inscrivant le numéro de la table : "))
        if num_file < 1 or num_file > 12:
            print("Veuillez entrer un numéro de table valide")

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
            for i in range(len(steps)):
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
    :return nodes, graph, start_node, end_node:
    """
    # read file
    constraint_table = read_file("Operational_research/constraint_tables/table_" + str(num_file) + ".txt")

    # initialize problem table
    tab_problem = Tab()

    # add cout to the problem table
    for i in range(0, len(constraint_table)):
        for j in range(0, len(constraint_table[i])):
            pass
            # tab_problem.cout.append([constraint_table[i][j]])

    # add command to the problem table

    # add provider to the problem table

    return tab_problem
