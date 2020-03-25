class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) if the LinkedList was empty when we start
        0(n) if LinkedList have items; we have to loop through the LinkedList
        until we get a node where it's next item is none
        """
        # counting the data
        self.count += 1
        # creating a new node
        new_node = Node(item)
        # check if the LinkedList is empty to make the new node the head
        if self.head is None:
            self.head = new_node
            self.tail =  new_node
            return
        # appending item to the tail
        self.tail.next = new_node
        self.tail = self.tail.next

    def reverse_iterative(self, llItems):
        """reverse items in a list
        0(n) if LinkedList have items; we have to loop through the LinkedList
        until we get a node where it's next item is none
        """
        # traverse through the ll and change next to prev
        print(type(llItems))
        print(llItems.tail)
        # cur_node = llItems.tail
        # self.head = cur_node
        # while cur_node.next:
        # ('A') -> ('B') -> ('C') -> ('D') -> ('F')
        # None <- ('A') <- ('B') <- ('C') <- ('D') <- ('F')
        # ('F') -> ('D') -> ('C') -> ('B') -> ('A')
        prev = None
        cur_node = llItems.head
        while cur_node:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next
        llItems.head = prev
        return llItems

    def reverse_recursive(self, llItems, prev=None, cur_node=None):
        prev = prev
        cur_node = cur_node
        llItems = llItems
        if not cur_node:
            llItems.head = prev
            return llItems
        if cur_node:
            next = cur_node.next
            cur_node.next = prev
            print("cur_node", cur_node, "prev", prev)
            prev = cur_node
            cur_node = next
            return self.reverse_recursive(llItems, prev=prev, cur_node=cur_node)

ll = LinkedList(['A', 'B', 'C', 'D', 'F'])
# print(ll, type(ll))
# print("reversed LinkedList iterative: ", ll.reverse_iterative(ll))
# print(ll)
print("reversed LinkedList recursive: ", ll.reverse_recursive(ll, cur_node=ll.head))
