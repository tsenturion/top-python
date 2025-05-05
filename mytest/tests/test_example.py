from my_pytest.example import reverse


def test_reverse():
    assert reverse("Src") == "crS"


def test_reverse_for_empty_string():
    assert reverse("") == ""

def test_stack():
    stack = []
    stack.append(1)
    stack.append(2)

    assert stack.pop() == 2
    assert stack.pop() == 1


def test_emtines():
    stack = []
    assert not stack
    stack.append(1)
    assert bool(stack)

    stack.pop()
    assert not stack