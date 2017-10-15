import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.decisiontree import *


training_data = pd.read_csv('data/train.csv')
testing_data = pd.read_csv('data/test.csv')


base = Decision_tree(training_data)


# 3 types of data, D for discrete C for continuous, B of binary
population_conditions = [
        ('Pclass', [1,2,3], "D"), 
        ('Sex', ['male', 'female'], "D"), 
        ('Age', 14, "C"),
        ('Fare', 50, "C"),
        ('Cabin', 'NaN', "B"),
        ('Embarked', ['C', 'Q', 'S'], "D")
        ]


# initialisation of the tree using the database
currents = [base]
for line in population_conditions:
    new = []
    for tree in currents:
        if line[2] == "C":
            tree.add_child(Decision_tree(tree.data_set[tree.data_set[line[0]] < line[1]]), line[0], line[1], '<')
            tree.add_child(Decision_tree(tree.data_set[tree.data_set[line[0]] >= line[1]]), line[0], line[1], '>=')
        elif line[2] == "D":
            [tree.add_child(Decision_tree(tree.data_set[tree.data_set[line[0]] == i]), line[0], i, '==') for i in line[1]]
        else:
            tree.add_child(Decision_tree(tree.data_set[tree.data_set[line[0]] == line[1]]), line[0], line[1], '==')
            tree.add_child(Decision_tree(tree.data_set[tree.data_set[line[0]] != line[1]]), line[0], line[1], '!=')

        new += tree.get_children()
    currents = new

currents = [base]
while len(currents) != 0:
    new = []
    print('###')
    for current in currents:
        print(len(current.get_children()), current.survive_chance)
        new += current.get_children()
    currents = new


print(base.accum_proba('Age', 14, '<'))

