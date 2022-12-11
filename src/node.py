
class Node:

    def __init__(self, operation):
        self.value = 0
        self.operation = operation

    def __str__(self):

        return str(self.value) + " " + self.operation
