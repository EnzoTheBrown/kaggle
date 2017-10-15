import pandas as pd
import numpy as np


class Decision_tree:
    def __init__(self, data_set):
        self.children = []
        self.data_set = data_set
        if len(data_set) != 0:
            self.survive_chance = len(data_set[data_set['Survived'] == 1]) / len(data_set)
        else:
            self.survive_chance = "NaN"

    def add_child(self, child, event, condition, op):
        self.children.append(
                {
                    'child': child,
                    'event': event,
                    'condition': condition,
                    'op': op
                    }

                )

    def get_children(self):
        return [child['child'] for child in self.children]

    @staticmethod
    def handle_op(op, left, right):
        return {
                '==': left == right,
                '!=': left != right,
                '<': left < right,
                '>=': left >= right
                }.get(op, False)

    def accum_proba(self, event, condition, op):
        if len(self.children) > 0:
            return 0
        elif self.children[0]['event'] == event:
            for child in self.children:
                if  self.handle_op(
                        child['op'],
                        child['condition'],
                        condition):
                    return child['child'].survive_chance
        else:
            return np.sum(
                    [
                        self.survive_chance*child['child'].\
                        accum_proba(event, condition, op)\
                        for child in self.children
                        ]
                    )

