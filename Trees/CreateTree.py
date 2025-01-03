#Creation of Tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # def __str__(self, level=0):
    #     rtn = " "*level+str(self.data)
    #
    #     return rtn


newBinaryTree = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")

# Now adding the leftchild and right Child to the Main Root Node

newBinaryTree.leftChild = hot
newBinaryTree.rightChild = cold

# adding the left and right child to the left Subtree of Hot
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee

# Adding the left and right Child to the left subtree of Tea
blackTea = TreeNode("BlackTea")
GreenTea = TreeNode("GreenTea")
tea.leftChild = blackTea
tea.rightChild = GreenTea

# Adding the left and right child in the right sub tree of cold
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
cold.leftChild = cola
cold.rightChild = fanta


def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


print("\nPre Order Traversal of binary Tree : \n")
preOrderTraversal(newBinaryTree)


# in order traversal of binary tree

def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


print("\nIn Order Traversal of binary Tree : \n")
inOrderTraversal(newBinaryTree)


def PostOrderTraversal(rootNode):
    if rootNode is None:
        return

    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


print("\nPost Order Traversal of binary Tree : \n")
PostOrderTraversal(newBinaryTree)

