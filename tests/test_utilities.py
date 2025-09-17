import pytest
import math
import numpy as np
from utilities import *

def test_sequence():
    assert sequence([1, 2]) == [1, 2]
    assert sequence((1, 2)) == (1, 2)
    assert sequence(1) == (1,)

def test_remove_all():
    assert remove_all(2, [1, 2, 3, 2]) == [1, 3]
    assert remove_all('a', 'banana') == 'bnn'
    s = {1, 2, 3}
    result = remove_all(2, s)
    assert result == {1, 3}

def test_unique():
    assert set(unique([1, 1, 2, 2, 3])) == {1, 2, 3}

def test_count():
    assert count([0, 1, True, False]) == 2

def test_multimap_and_items():
    items = [('a', 1), ('a', 2), ('b', 3)]
    mm = multimap(items)
    assert mm == {'a': [1, 2], 'b': [3]}
    pairs = list(multimap_items(mm))
    assert set(pairs) == set(items)

def test_product():
    assert product([2, 3, 4]) == 24

def test_first():
    assert first([10, 20]) == 10
    assert first([], default=5) == 5

def test_is_in():
    a = [1,2,3]
    x = a[0]
    assert is_in(x, a) is True
    assert is_in(100, a) is False

def test_power_set():
    ps = power_set([1, 2, 3])
    assert (1, 2) in ps
    assert (3,) in ps

def test_vector_add_and_scalar_vector_product():
    assert vector_add((1, 2), (3, 4)) == (4, 6)
    assert np.array_equal(scalar_vector_product(2, [1, 2, 3]), [2, 4, 6])

def test_distance_functions():
    a, b = (0, 0), (3, 4)
    assert euclidean_distance(a, b) == 5
    assert manhattan_distance(a, b) == 7
    assert hamming_distance([1,0,1], [0,0,1]) == 1

def test_activation_functions():
    assert relu(-1) == 0
    assert relu(5) == 5
    assert leaky_relu(-2, alpha=0.1) == -0.2
    assert math.isclose(sigmoid(0), 0.5)
    assert tanh(0) == 0

def test_rounder_and_num_or_str():
    assert rounder([1.123456], 2) == [1.12]
    assert num_or_str("5") == 5
    assert num_or_str("3.5") == 3.5
    assert num_or_str("abc") == "abc"

def test_normalize():
    assert normalize([1, 1, 2]) == [0.25, 0.25, 0.5]
    d = {'a': 1, 'b': 3}
    normalized = normalize(d)
    assert math.isclose(normalized['a'], 0.25)
    assert math.isclose(normalized['b'], 0.75)

def test_memoize():
    calls = []
    def f(x):
        calls.append(x)
        return x * 2
    mf = memoize(f)
    assert mf(3) == 6
    assert mf(3) == 6
    assert calls == [3]

def test_priority_queue():
    pq = PriorityQueue(f=lambda x: x)
    pq.append(3)
    pq.append(1)
    pq.append(2)
    assert pq.pop() == 1
    assert pq.pop() == 2
    assert pq.pop() == 3

def test_expr_basic():
    x = Symbol('x')
    y = Symbol('y')
    e = x + y
    assert isinstance(e, Expr)
    assert e.op == '+'
    assert e.args[0] == x
    assert e.args[1] == y

def test_expr_subexpressions():
    x = Symbol('x')
    y = Symbol('y')
    e = x + y
    subs = list(subexpressions(e))
    assert x in subs
    assert y in subs
    assert e in subs
