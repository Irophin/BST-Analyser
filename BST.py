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
        self.left  = left
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
        if not tab:
            return None

        tree = BST.smart_plant(None, tab[0])
        for i in range(1, len(tab)):
            tree = tree.smart_plant(tab[i])
            print(tree)

        return tree
    
    
    @staticmethod
    def smart_create_bst(tab):
        """ Create a balanced binary search tree from a list of values
                
            Parameters:
                tab(list<any>) : the list of values

            Returns:
                BST  : the tree
                None : if the list is empty
        """
        if not tab:
            return None
        
        copy_tab = tab.copy()
        copy_tab.sort()

        recurise_median = []
        BST.recursive_median(copy_tab, recurise_median, 0, len(copy_tab)-1)

        tree = BST(recurise_median[0])
        for i in range(1, len(recurise_median)):
            tree.plant(recurise_median[i])

        return tree
    

    @staticmethod
    def recursive_median(values, new_values, i, j):
        """ Procedure to complete the array new_values with the successive medians of the array values
            
            Parameters:
                values(list<any>) : the list of values
                new_values(list<any>) : the list of medians
                i(int) : the index of the first element of the array values
                j(int) : the index of the last element of the array values
            
            returns:
                None : In any cases
        """

        if (i > j):
            return None
        
        mediane = (i+j)//2
        new_values.append(values[mediane])

        BST.recursive_median(values, new_values, i, mediane-1)
        BST.recursive_median(values, new_values, mediane+1, j)


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
            self.left = BST.plant(self.left, value)
        else:
            self.right = BST.plant(self.right, value)

        return self


    def smart_plant(self, value):

        if self is None:
            return BST(value)
        
        if value < self.value:
            self.left = BST.smart_plant(self.left, value)
        else:
            self.right = BST.smart_plant(self.right, value)

        balance = BST.height(self.left) - BST.height(self.right)

        # if the tree is unbalanced on the left side
        if balance > 1:
            if value < self.left.value:
                return self.rotate_right()
            else:
                self.left = BST.rotate_left(self.left)
                return self.rotate_right()

        # if the tree is unbalanced on the right side
        if balance < -1:
            if value > self.right.value:
                return self.rotate_left()
            else:
                self.right = BST.rotate_right(self.right)
                return self.rotate_left()

        return self


    def rotate_right(self):
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        return left_child

    def rotate_left(self):
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        return right_child



    def size(self):
        """ Returns the size of the tree
            
            Returns:
                int : the size of the tree
        """
        if self == None:
            return 0
        return 1 + BST.size(self.left) + BST.size(self.right)
    

    def height(self):
        """ Returns the height of the tree
            
            Returns:
                int : the height of the tree
        """
        if self == None:
            return -1
        return 1 + max(
            BST.height(self.left),
            BST.height(self.right),
        )        

    def search(self, value):
        """ Search a value in the tree

            Parameters:
                value(any) : the value to search
            
            Returns:
                BST   : the node containing the value
                False : if the value is not in the tree
        """
        if self is None:
            return False

        if (self.value == value):
            return self
  
        if (self.value < value):
            return BST.search(self.right,value)
        else:
            return BST.search(self.left,value)
    

    def maximum_node(self):
        """ Get the node having the maximum value of the tree

            Returns:
                BST   : the node containing the maximum value
                False : if the value is not in the tree
        """
        if self is None:
            return None
        elif self.right is None:
            return self
        self.right.maximum_node()
        

    def minimum_node(self):
        """Get the node having the minimum value of the tree

            Returns:
                BST   : the node containing the minimum value
                False : if the value is not in the tree
        """
        if self is None:
            return None
        elif self.left is None:
            return self
        self.left.minimum_node()


    def delete_node(self, key):
        """ Delete the node having the key as value while keeping the structure of a BST

            Parameters:
                key(any) : the value to delete

            Returns:
                BST  : If the node was successfully deleted
                None : If the node to delete doesn't exist in the tree, or if the tree has only the value to delete

        """
        # If the tree is empty
        if self is None:
            return None
        
        # We traverse the tree using an iterator
        current = self
        parent  = None

        while current:
            if key < current.value:
                # If the wanted value is lower than the current node value, we move on the left subtree
                parent  = current
                current = current.left
            elif key > current.value:
                # If the wanted value is greater than the current node value, we move on the right subtree
                parent  = current
                current = current.right
            else:
                # If the wanted value is equal to the current node value, the node is deleted according to its subtrees
                if current.left is None:
                    # If we are at the root, the tree become its right subtree
                    if parent is None: 
                        self = self.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    return self
                elif current.right is None:
                    # If we are at the root, the tree become its left subtree
                    if parent is None: 
                        self = self.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    return self
                else:
                    # If the current node has two subtrees
                    # The node is replaced by its successor according the Inorder Traversal (the smallest to the right) 
                    successor = current.right
                    while successor.left:
                        successor = successor.left
                    current.value = successor.value
                    current.right = current.right.delete_node(successor.value)
                    return self


    def inorder(self, tab = []):
        """ Print the values of the tree using the Inorder Traversal

            Parameters:
                tab(list<any>) : the list of values sorted by the Inorder Traversal

            Returns:
                None : In any cases, especially when the tree has no value
        """
        if self is None:
            return None

        BST.inorder(self.left, tab)
        tab.append(self.value)
        BST.inorder(self.right, tab)
        if len(tab) == self.size():
            return tab
        

    
    def preorder(self, tab = []):
        """ Print the values of the tree using the Preorder Traversal

            Parameters:
                tab(list<any>) : the list of values sorted by the Preorder Traversal

            Returns:
                None : In any cases, especially when the tree has no value
        """
        if self is None:
            return None
        
        tab.append(self.value)
        BST.preorder(self.left)
        BST.preorder(self.right)

        if len(tab) == self.size():
            return tab

    
    def postorder(self, tab = []):
        """ Print the values of the tree using the Postorder Traversal

            Parameters:
                tab(list<any>) : the list of values sorted by the Postorder Traversal

            Returns:
                None : In any cases, especially when the tree has no value
        """
        if self is None:
            return None

        BST.postorder(self.left)
        BST.postorder(self.right)
        tab.append(self.value)

        if len(tab) == self.size():
            return tab

    
    def levelorder(self, tab = []):
        """ Print the values of the tree using the Levelorder Traversal/Breadth-first Search

            Parameters:
                tab(list<any>) : the list of values sorted by the levelorder Traversal

            Returns:
                None : In any cases, especially when the tree has no value
        """
        if self is None:
            return None

        queue = [self]

        while len(queue) > 0:
            current_node = queue.pop(0)
            tab.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            
            if current_node.right is not None:
                queue.append(current_node.right)

        return tab


""" Test Results """
if __name__ == "__main__":
    tab  = [ 21, 8, 9, 3, 15, 19, 20, 7, 3, 2, 1, 5, 6, 4, 13, 14, 12, 17, 16, 18]
    tree = BST.create_bst(tab)

    #Basic methods
    print("Tree     : ", tree)
    print("Size     : ", BST.size(tree))
    print("Height   : ", BST.height(tree))

    search = BST.search(tree, 5)
    print("Search 5 : ", search != None and search.value == 5)

    #Traversal methods
    print("Inorder Traversal    : ", tree.inorder())
    print("Preorder Traversal   : ", tree.preorder())
    print("Postorder Traversal  : ", tree.postorder())
    print("Levelorder Traversal : ", tree.levelorder())

    #Deletion method
    print(tree.delete_node(18))