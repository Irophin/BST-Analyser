from binarytree import Node

class BST(Node):
    """ Binary Search Tree class
    
        Attributes:
            value(any) : the value of the node
            left (BST) : the left child
            right(BST) : the right child
    """

    def __init__(self, value, left=None, right=None):
        """ Constructor of the class
            
            Parameters:
                value(any) : the value of the node
                left (BST) : the left child
                right(BST) : the right child
        """
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def create_bst(tab):
        """ Create a binary search tree from a list of values
                
            Parameters:
                tab(list<any>) : the list of values

            Returns:
                BST  : the tree
                None : if the list is empty
        """
        if len(tab) == 0:
            return None

        tree = BST.plant(None, tab[0])
        for i in range(1, len(tab)):
            tree.plant(tab[i])
        return tree

    def plant(self, value) :
        """ Insert a new value in the tree
            
            Parameters:
                value(any) : the value to insert

            Returns:
                BST  : the new tree if it doesn't exist yet
                None : if the tree already exists
        """ 
        if (self == None):
            return BST(value)
        
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.plant(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.plant(value)

if __name__ == "__main__":
    tab = [21,8,9,3,15,19,20,7,3,2,1,5,6,4,13,14,12,17,16,18]
    bst = BST.create_bst(tab)
    print(bst)