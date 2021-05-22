
# We represent Binary tree as a tree of Node data structure
# Each node can have atmost 2 nodes.
# Nodes at the last level of a Binary tree are called leaf nodes as they
# donot have childrens

class Node(object):
    """ We present a Node within a binary Tree using Node Class.
    Each Node have a data state & left,right state to capture reference
    to left child & right child node.
    Initially, left & right node state is None. Until a Node is added
    to it as a child using Binary Tree Class's behaviour/method.

    All the behaviours like: adding of child, get data, set data
    for a Node are defined within this class.

    However, as discussed earlier according to OOPS concepts,
    Binary Tree class can get,set value of a node class using it's method.
    This servers as a abstraction for the user.

    eg: for adding a node child to a node. A Binary Tree
    behaviour/method will only have to call that node's method
    of adding a child. Rest we will see during examples how it is implemented.
    """

    def __init__(self, data):
        """ we Initialize a Node with value based as data.
        And left & right child referring to None i.e no node.
        """
        self.data= data
        self.left= None
        self.right= None

class BinaryTree(object):
    """
    Used to define BinaryTree.
    A Binary Tree contains root as state.
    We assume root  value will be provided whenever, an object of
    Binary Tree is created. Thus we will take root data value will
    be passed to the class's constructor i.e __init__ method.

    """
    def __init__(self,root_data):
        """ We assume when a BinaryTree instance is created.
         Data value for root node will always be passed.
         And we instantiate root with a Node(root_data)
        """
        self.root= Node(root_data)



if __name__=="__main__":

    binary_tree1= BinaryTree(1)

    # Manually adding a node to Binary Tree
    binary_tree1.root.left= Node(2)
    binary_tree1.root.right= Node(3)
    #   1
    #  / \
    # 2   3
    binary_tree1.root.left.left= Node(4)
    binary_tree1.root.left.right= Node(5)

    #         1
    #       /   \
    #      2     3
    #     / \
    #    4   5

