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
        """

        if self._length == 0:
            return None
        
        temp = self.head

        if self._length == 1:
            self.head = None
            self.tail = None

            self._length -= 1

            return temp.value
        
        curr = temp
        prev = temp

        while curr.next:
            prev = curr
            curr = curr.next
        
        self.tail = prev
        self.tail.next = None

        return curr.value


    def prepend(self, item: Any) -> bool:
        """Insert an item add the start of the LinkedList.
        
        Creates a new LinkedList if it is empty.

        Args:
            item (Any): The item to be inserted.
        
        Returns:
            (bool): Returns True if the item is correctly inserted.
        """
        new_node = Node(item)

        if not self.head or self._length == 0:
            self.head = new_node
            self.tail = new_node
            self._length += 1

            return True
        
        temp = self.head
        new_node.next = temp
        self.head = new_node

        self._length += 1

        return True

    def pop_first(self):
        """Return and remove from the LinkedList the first item.
        
        Returns:
            (Any): The first item fromt the LinkedList.
        
        Raises:
            (ValueError): If the LinkedList is empty.
        """
        if self._length == 0:
            return None
        
        temp = self.head

        if self._length == 1:
            self.head = None
            self.tail = None
            self._length -= 1
            return temp
        
        self.head = self.head.next
        self._length -= 1
        
        temp.next = None

        return temp

    def get(self, index: int):
        """Returns the item at the index position.
        
        Args:
            index (int): The index position to retrieve the item from the LinkedList.

        Returns:
            (Any): The item at the index position.

        Raises:
            (IndexError): If the index is negative or greater than the size of the LinkedList.    
        """

        if index < 0 or index >= self._length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp

    def set_value(self, index: int, item: Any):
        """"""
        if index < 0 or index >= self._length:
            return False

        node = self.get(index)
        node.value = item

        return True
        
    def insert(self, index: int, item: Any):
        """"""
        if index == 0:
            return self.prepend(item)
        
        if index < 0 or index > self._length:
            return False
        
        if index == self._length:
            return self.append(item)
         
        temp = self.get(index - 1)

        swap = Node(item)
        swap.next = temp.next
        temp.next = swap
        self._length += 1

        return True

    def remove(self, index: int):
        """"""
        if index < 0 or index >= self._length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self._length:
            return self.pop()
        
        previous_node = self.get(index - 1)
        node_to_be_removed = previous_node.next

        previous_node.next = node_to_be_removed.next

        self._length -= 1

        return node_to_be_removed
    
    def reverse(self):
        if self._length == 0 or self._length == 1:
            return True

        swap = self.head
        self.head = self.tail
        self.tail = swap

        before = None
        after = swap.next

        for _ in range(self._length):
            after = swap.next
            swap.next = before
            before = swap
            swap = after
        
        return True

if __name__ == "__main__":
    
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    print(my_linked_list)
    tail = my_linked_list.reverse()
    # print(f"tail.value: {tail.value} | tail.next: {tail.next.value}")
    print(my_linked_list)

