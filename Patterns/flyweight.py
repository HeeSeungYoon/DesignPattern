class TreeManager:
    def __init__(self) -> None:
        self.treeArray = []

    def displayTrees(self):
        for tree in self.treeArray:
            tree.display(3,5,10)

class Tree:
    def __init__(self) -> None:
        self.xCoord=0
        self.yCoord=0
        self.age=0
    
    def display(self, x, y, age):
        pass