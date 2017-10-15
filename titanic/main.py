import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


training_data = pd.read_csv('data/train.csv')
testing_data = pd.read_csv('data/test.csv')

def survived_chance(population, condition, data_set):
    population_data = data_set[data_set[population] == condition]
    return len(
            population_data[population_data['Survived'] == 1]
            )/ len(population_data)

class Decision_tree:
    def __init__(self, data_set, population, condition, op):
        self.children = []
        self.condition = condition
        self.op = op
        self.population = population
        self.data_set = data_set
        if len(data_set) != 0:
            self.survive_chance = len(data_set[data_set['Survived'] == 1]) / len(data_set)
        else:
            self.survive_chance = "NaN"

    def displayProb(self):
        print(self.survive_chance)
        for tree in self.children:
            tree.displayProb()

    def accum_proba(self, events):
        (pop, cond, op) = event[0]


base = Decision_tree(training_data, "None", "None", "None")
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
            tree.children.append(Decision_tree(tree.data_set[tree.data_set[line[0]] < line[1]], line[0], line[1], '<'))
            tree.children.append(Decision_tree(tree.data_set[tree.data_set[line[0]] >= line[1]], line[0], line[1], '>='))
        elif line[2] == "D":
            [tree.children.append(Decision_tree(tree.data_set[tree.data_set[line[0]] == i], line[0], i, '==')) for i in line[1]]
        else:
            tree.children.append(Decision_tree(tree.data_set[tree.data_set[line[0]] == line[1]], line[0], line[1], '=='))
            tree.children.append(Decision_tree(tree.data_set[tree.data_set[line[0]] != line[1]], line[0], line[1], '!='))

        new += tree.children
    currents = new

print(testing_data)






