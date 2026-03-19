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

    ll_mix = LinkedList("1")
    ll_mix.append(2)
    ll_mix.append(4)
    ll_mix.append("b")

    pop_mix = ll_mix.pop()

    assert pop == 5
    assert ll.__str__() == '[4, 3, 2]'
    assert pop_mix == "b"
    assert ll_mix.__str__() == '[\'1\', 2, 4]'




def test_linked_list_prepend():
    pass


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