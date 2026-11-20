import pytest

from stack import Stack


def test_pop_returns_last_pushed_first():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_pop_and_peek_on_empty_stack_return_none():
    stack = Stack()
    assert stack.pop() is None
    assert stack.peek() is None
    assert stack.is_empty()


def test_peek_does_not_remove_element():
    stack = Stack()
    stack.push(5)
    assert stack.peek() == 5
    assert stack.size() == 1


@pytest.mark.parametrize("value", ["a", 1.5, None])
def test_push_non_integer_raises_error(value):
    with pytest.raises(TypeError):
        Stack().push(value)
