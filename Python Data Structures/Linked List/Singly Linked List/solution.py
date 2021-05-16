


class LinkedList:
    """
    We represent a Linked List using Linked List class
    having states and behaviours
    states of SLL includes- self.head as an instance variable.
    Behaviour of LL class will include any behaviours that we implement on a Singly list list.

    Whenever a LL instance is initialized
    it will have zero nodes withing itself.
    Thus while initializing a LL we make self.head as None (refer __init__)."""

    def __init__(self):
        self.head=None

    def append_node(self,data):
        """ Let's write a LL behaviour which will append a data Node at last of the LL.
        We will pass data as a method argument and the function will instantiate a new node
        and append it to the LL instance, accordingly.

        There can be two cases- (1) Either the LL is compeltely empty i.e head is None Or
        or (2) The LL have some values- in this case we will search for the last Node.

         A last Node is defined as Node for which, the next state value is None.
         To search for the last Node, we will traverse the LL instance till a node which is
         having next state property is found. Once it is found we call that Node as last Node
         and initialize it's next value as reference to our new node.

         In All cases a New Node has to be made with data, passed as an argument."""

        # In All cases a New Node has to be made with data, passed as an argument.
        new_node = Node(data)

        # In Case the LL is empty.
        if self.head is None:
            self.head = new_node
            # By default new_node's next is == None.
            return

        # Search for last_node: as Node having next state value as None.
        # One way is to run a for loop and break whenever a Node with next value None is found.
        # however, using break is not a good programming method.
        # Wherever, you find a situation to run a loop until a condition is matched, like in this case
        # we can use While loop of python.
        # condition here: last_node.next is not None.
        last_node = self.head

        # is next pointing to Null, if No, move to next Node, otherwise come out of the loop
        while last_node.next is not None:
            last_node = last_node.next
        # found last_node
        last_node.next = new_node
        # new_node by default have next values as None.
        return

    def print_nodes(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        current_node = self.head
        while current_node is not None:
            print("current_nod data is: ",current_node.data)
            current_node = current_node.next

        print("Print_nodes complete")
        return


class Node:
    """
    Whenever, a Node is defined it has two states: (1) Data & (2) Next: reference to the next node.
    The (1) data can contain any type of data including built-int types or an class object.
    Now whenever a a new Node is created it can have either None data & then we class a behaviours method of
    Node class to insert data or we can include data within the constructor as an argument. TO safe time
    we will do the later here.

    Also, whenever a new Node is created it will have next reference value as None. As currently, it's
    just a standalone Node and is not added to any data structure like LL.

    Any Behaviours like data change within a Node will be written & explained in Node Class methods.
    While any change like addition or Deletion og Nodes will be be written as behaviours of LL i.e LL class Method."""
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__=="__main__":
    """Driver code
    (1) Create LL
    (2) Append nodes to it"""

    LL1 = LinkedList()
    LL1.append_node(10)
    LL1.append_node(11)
    LL1.append_node('abc')
    LL1.print_nodes()