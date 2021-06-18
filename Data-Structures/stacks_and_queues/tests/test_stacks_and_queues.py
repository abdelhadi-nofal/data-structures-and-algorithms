from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Node, Queue,Stack
import pytest


# Stack Test

def test_version():
    assert __version__ == '0.1.0'


def test_stack_push(stack_3vals):
    actual = stack_3vals.top.value
    expected = 'd'
    assert actual == expected

def test_stack_pop(stack_3vals):
    actual = stack_3vals.pop()
    expected = 'd'
    assert actual == expected
    # assert stack_3vals.top.value == -1

def test_stack_peek(stack_3vals):
    actual = stack_3vals.peek()
    expexted = 'd'
    assert actual == expexted
    assert stack_3vals.top.value == 'd'

def test_stack_isEmpty(stack_3vals):
    assert stack_3vals.isEmpty() == False

@pytest.fixture
def stack_3vals():
    stack =Stack()
    stack.push(3)
    stack.push(-1)
    stack.push('d')
    return stack

# ////////////////////////////////////////////////////////////////////////////

# Queue Test

def test_queue_enqueue(queue_3vals):
    actual = queue_3vals.front.value
    expected = 3
    assert actual == expected


def test_queue_dequeue(queue_3vals):
    actual = queue_3vals.dequeue()
    expected = 3
    assert actual == expected
    assert queue_3vals.front.value == -8

def test_queue_peek(queue_3vals):
    actual = queue_3vals.peek()
    expected = 3
    assert actual == expected
    assert queue_3vals.front.value == 3

def test_queue_isEmpty(queue_3vals):
    assert queue_3vals.isEmpty() == False

@pytest.fixture
def queue_3vals():
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(-8)
    queue.enqueue('z')
    queue.enqueue('a')
    return queue
