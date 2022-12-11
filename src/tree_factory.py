import random
from treelib import Tree

from node import Node


class TreeFactory:
    operations = ["AND", "OR", "IF", "ELSE", "FOR"]

    def generate_operations(self):
        random_operation = random.choice(self.operations)
        self.tree.create_node(1, 1, data=Node(random_operation))

        for i in range(2, 6):
            start = pow(2, i - 1)
            end = pow(2, i)
            if end == 32:
                end = 31
            for j in range(start, end):
                random_operation = random.choice(self.operations)
                parent = int(j/2)
                self.tree.create_node(j, j, parent, data=Node(random_operation))


    def __init__(self):
        self.score = 0
        self.tree = Tree()
        self.generate_operations()

    def populate_tree(self, values):

        for i in range(15, 30):
            self.tree[i].data.value = values[i - 15]

    def compute_operations_in_range(self, start, end):
        for i in range(start, end):
            self.tree[i].data.value = self.compute_operation(self.tree[i].data.operation, self.tree[i * 2].data.value, self.tree[i * 2 + 1].data.value)


    def compute_operations(self):
        self.compute_operations_in_range(8, 15)
        self.tree[15].data.value = self.tree[30].data.value
        self.compute_operations_in_range(4, 8)
        self.compute_operations_in_range(2, 4)
        self.tree[1].data.value = self.compute_operation(self.tree[1].data.operation, self.tree[2].data.value, self.tree[3].data.value)
        return self.tree[1].data.value

    def compute_operation(self, operation, a, b):
        if operation == "AND":
            return self.compute_and(a, b)
        elif operation == "OR":
            return self.compute_or(a, b)
        elif operation == "IF":
            return self.compute_if_else(a, b)
        elif operation == "ELSE":
            return self.compute_if_else(b, a)
        else:
            return self.compute_for(a, b)

    def compute_if_else(self, a, b):
        if abs(a - 0.5) < abs(b - 0.5):
            return (a * 5 + b * 3) / 8
        else:
            return (b * 3 + a * 5) / 8

    def compute_and(self, a, b):
        return (a + b + 0.0001) / 2

    def compute_or(self, a, b):
        num = random.randint(0, 1)
        if num:
            return a
        else:
            return b

    def compute_for(self, a, b):
        for i in range(5):
            num = random.randint(0, 1)
            if num:
                a = (a + b + 0.0001) / 2
            else:
                b = (a + b + 0.0001) / 2
        return (a + b + 0.0001) / 2

    def show(self):
        for i in range(1, 31):
            print("node " + str(i) + " with operation: " + str(self.tree[i].data.operation))





