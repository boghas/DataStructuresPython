from linkedlist.linked_list import LinkedList


def test_linked_list_constructor():
    ll = LinkedList(4)
    ll_str = LinkedList("a")
    ll_fl = LinkedList(3.89)

    assert ll.head.value == 4
    assert ll_str.head.value == "a"
    assert ll_fl.head.value == 3.89


def test_linked_list_print():
    pass


def test_linked_list_append():
    pass

def test_linked_list_len():
    pass


def test_linked_list_pop():
    ll = LinkedList(4)
    ll.append(3)
    ll.append(2)
    ll.append(5)

    pop = ll.pop()

    assert pop == 5
    assert str(ll) == '[4, 3, 2]'

    ll_mix = LinkedList("1")
    ll_mix.append(2)
    ll_mix.append(4)
    ll_mix.append("b")

    pop_mix = ll_mix.pop()

    assert pop_mix == "b"
    assert ll_mix.__str__() == '[\'1\', 2, 4]'

    ll = LinkedList(1)
    val = ll.pop()

    assert ll == 1
    assert len(ll) == 0
    assert ll.head == None


def test_linked_list_prepend():
    ll = LinkedList(2)
    ll.append(3)
    ll.append(5)

    ll.prepend(0)

    assert ll.head.value == 0
    assert len(ll) == 4

    ll = LinkedList(1)
    ll.pop()

    ll.prepend(2)

    assert ll.head.value == 2
    assert len(ll) == 1


def test_linked_list_pop_first():
    pass


def test_linked_list_get():
    pass


def test_linked_list_set():
    pass


def test_linked_list_remove():
    pass


def test_linked_list_reverse():
    pass


def test_linked_list_repr():
    pass