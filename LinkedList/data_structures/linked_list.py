from nodes.nodes import Node
    

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, value: int):
        """Adds a new item to the list."""
        if self.head is None:
            self.head = Node(value)
            self.length += 1
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            
            last_node.next = Node(value)
            self.length += 1

    def insert(self, value: int, index: int):
        """Insert a new item at a given position."""

        if self.head is None:
            raise IndexError("The list is empty!")
        
        if index > self.length:
            raise IndexError("The index is out of range!")
        
        new_node = Node(value)
        last_node = self.head
        
        if index == 0:
            new_node.next = last_node
            self.head = new_node
            self.length += 1
        
        else:
            index -= 1
            while last_node.next:
                last_node = last_node.next
                index -= 1

                if index == 0:
                    break

            new_node.next = last_node.next
            last_node.next = new_node
            self.length += 1

    def __len__(self) -> int:
        """Returns the size of the list."""

        return self.length         

    def delete(self, value: int):
        """Delete an item from the list."""

        if not self.head:
            raise ValueError("The List is empty!")
        
        last_node = self.head
        
        if last_node.value == value:
            self.head = last_node.next
            self.length -= 1
        
        else:
            while last_node.next:
                if last_node.next.value == value:
                    last_node.next = last_node.next.next
                    self.length -= 1
                    return
                
                last_node = last_node.next
                

    def remove(self, index: int):
        """Remove an element from a certain position"""

        if not self.head:
            raise IndexError("List is empty!")
        
        last_node = self.head

        if index == 0:
            self.head = last_node.next
            self.length -= 1
        
        else:
            index -= 1

            while last_node.next:
                if index == 0:
                    last_node.next = last_node.next.next
                    self.length -= 1
                    return
            
                last_node = last_node.next
                index -= 1
            
            raise IndexError("Index out of range!")

    def __repr__(self) -> str:
        """Returns a string representation of the list."""
        
        values = "["
        if self.head is not None:
            last_node = self.head
            values += str(last_node.value)

            while last_node.next:
                last_node = last_node.next
                values += ", " + str(last_node.value)          
        values += "]"
        return values