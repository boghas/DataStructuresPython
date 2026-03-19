from typing import Any


class Node:

    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    """"""

    def __init__(self, value: Any):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self._length = 1
    
    def __str__(self) -> str:

        if not self.head:
            return "[]"
        
        temp = self.head
        items = f"["
        
        while temp:
            items += f"{temp.value!r}, "
            temp = temp.next
        
        items = items[:-2] + "]"

        return items
    
    def __repr__(self) -> str:
        pass

    def __len__(self) -> int:

        return self._length
    
    def append(self, item: Any):
        """Append an item at the end of the LinkedList.

        Creates a new LinkedList if it is empty.
        
        Args:
            item (Any): The item to append.
        """

        if not self.head:
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            temp.next = Node(item)
            self.tail = temp.next

        self._length += 1
    
    def pop(self) -> Any:
        """Return and remove from the LinkedList the last item.
        
        Returns:
            (Any): The last item fromt the LinkedList.
        
        Raises:
            (ValueError): If the LinkedList is empty.
        """

        if not self.head:
            raise ValueError("The LinkedList is empty!")
        
        value = self.tail.value

        temp = self.head
        while temp.next.next:
            temp = temp.next

        self.tail = temp
        self.tail.next = None

        self._length -= 1

        return value

    def prepend(self, item: Any):
        """Insert an item add the start of the LinkedList.
        
        Creates a new LinkedList if it is empty.

        Args:
            item (Any): The item to be inserted.
        """

        if not self.head:
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
            self._length += 1
        
        temp = self.head
        new_node = Node(item)
        new_node.next = temp
        self.head = new_node

        self._length += 1

    def pop_first(self):
        """Return and remove from the LinkedList the first item.
        
        Returns:
            (Any): The first item fromt the LinkedList.
        
        Raises:
            (ValueError): If the LinkedList is empty.
        """

        if not self.head:
            raise ValueError("The LinkedList is empty!")
        
        temp = self.head
        self.head = temp.next

        self._length -= 1

        return temp.value

    def get(self, index: int):
        """Returns the item at the index position.
        
        Args:
            index (int): The index position to retrieve the item from the LinkedList.

        Returns:
            (Any): The item at the index position.

        Raises:
            (IndexError): If the index is negative or greater than the size of the LinkedList.    
        """

        if index >= self._length or index < 0:
            raise IndexError("LinkedList index out of range")
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp.value

    def set(self, index: int, item: Any):
        """"""
        if index >= self._length or index < 0:
            raise IndexError("LinkedList index out of range")
        
        temp = self.head

        for _ in range(index - 1):
            temp = temp.next
        
        new_node = Node(item)
        new_node.next = temp.next.next
        temp.next = new_node
        
    def insert(self, index: int, item: Any):
        """"""
        if index >= self._length or index < 0:
            raise IndexError("LinkedList index out of range")
        
        temp = self.head

        for _ in range(index - 1):
            temp = temp.next
        
        new_node = Node(item)
        new_node.next = temp.next
        temp.next = new_node

    def remove(self, index: int):
        """"""
        if index >= self._length or index < 0:
            raise IndexError("LinkedList index out of range")
        
        if index == 0:
            self.pop_first()
            return
        
        if index == self._length - 1:
            self.pop()
            return
        
        temp = self.head

        for _ in range(index - 1):
            temp = temp.next

        temp.next = temp.next.next

    def reverse(self):
        pass
    
if __name__ == "__main__":
    ll = LinkedList(1)

    ll.append(2)
    ll.append(3)
    print(ll)

    ll.prepend(5)
    print(ll)

    ll.pop_first()
    print(ll)

    print(ll.get(1))

    ll.set(2, 5)
    print(ll)

    ll.insert(1, 16)
    print(ll)

    ll.remove(1)
    print(ll)