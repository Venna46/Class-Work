#linked lists were created to overcome various drawbacks associated with
#storing data in regular lists and arrays, as outlined below:
#EASE OF INSERTION AND DELETION,
#They store elements in various, non-contiguous memory locations and connect them through pointers to subsequent nodes.
#WE JUST MODIFY NODES

#2. THE ASPECT OF DYNAMIC SIZE, In arrays and lists we conduct complex operations to add
#more memory blocks whenever we add new items.
#linked lists can grow and shrink dynamically

#MEMORY EFFICIENCY: Elements are allocated memory as they are added.

#A NODE is an element that stores data and reference to the next node_node in the sequence

class Node:
    def __init__(self, data):
        self.data = data     #Assigns the given data to the node
        self.next = None     #set the next attribute pointer to null (#Assigns the given data to the node)
        #As we continue to add new nodes to the linked list, this attribute will be updated to point to the subsequent node
"""
We will start by initializing the linked list which will encapsulate all the operations for managing the nodes, such as insertion and removal
"""

class LinkedList:
    def __init__(self):
        self.head = None

#The 'init' method is a special method in python classes, known as a constructor.
#It is called when an object is created from the class, and it allows the class to initialize attributes.
#By setting self.head to none, we are stating that the linked list is initially empty.
#And that there are no nodes in the list to point to.
# We will now proceed to populate the list by inserting nodes


    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#Every time you call the above method, a new node is created with your specified data.
#The next pointer of this new node is set to the current head of the list,
#which will place this node in front of the existing nodes.
#Finally, the newly created node is made the head of the list.

    def printList(self):
        temp = self.head   #start from the head of the list
        while temp:
            print(temp.data, end=' ') #print data in current node

            temp = temp.next #move to the next node
        print()


    #Inserting a new node at the end of the list.
    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data) #Create a new node

        if self.head is None:
            self.head = new_node #if the list empty, make the new node the head
            return None

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        return None

    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" #If empty, return this string
        self.head = self.head.next #If not empty, remove the head by making the next node the new head
        return None

    def deleteFromEnd(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None #If there is only one node, remove the head by making it none
            return None
        temp = self.head
        while temp.next.next: #Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None  #Remove the last node by setting the next pointer of the second-last node to None
        return None

    #Searching the linked list for a specific value
    def search(self, value):

        current = self.head  #start with the head of the list
        position = 0  #counter to keep track of the position
        while current:
            if current.data == value:
                return f"Value '{value}' found at the position {position}" #print the value if a match is found
            current = current.next
            position +=1
        return f"Value '{value}' not found in the list"


if __name__ == '__main__':
    #Create a new LinkedList instance
    llist = LinkedList()
    #Insert each letter at the beginning using the method we created
    llist.insertAtTheBeginning("fox")
    llist.insertAtTheBeginning("brown")
    llist.insertAtTheBeginning("quick")
    llist.insertAtTheBeginning("The")

    #Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    #print the list
    llist.printList()

    llist.insertAtTheEnd("jumps over the fence")
    llist.printList()

    #Deleting nodes from the beginning and end
    llist.deleteFromBeginning()
    print("List after deletion: ")
    llist.printList()

    #Search for 'quick' and 'lazy' in the list
    print(llist.search('quick')) #expected to find
    print(llist.search('lazy'))  #expected not to find
