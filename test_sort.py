"""
Тесты
"""
import sorting
import pytest

def test_bubble_smoke():
    test_list = [3, 1, 4, 5, 2]
    result = sorting.bubble_sort(test_list)
    assert result == [1, 2, 3, 4, 5]


def test_bubble_empty():
    test_list = []
    result = sorting.bubble_sort(test_list)
    assert result == []


def test_bubble_negative():
    test_list = [3, -1, 4, 5, -2]
    result = sorting.bubble_sort(test_list)
    test_list.sort()
    assert result == test_list


def test_bubble_not_integer():
    test_list = [3, 'one', 4, 5, '-2']
    with pytest.raises(RuntimeError):
        sorting.bubble_sort(test_list)