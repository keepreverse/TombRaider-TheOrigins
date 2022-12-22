"""
Bubble sort.
In the entities update, their relative order will not change too much between every frame.
So the bubble_sort for entities is a good choice.
Time complexity nearly O(n).
"""


def bubble_sort(_list, _compare):
    for i in range(len(_list)):
        for j in reversed(range(1, i + 1)):
            if _compare(_list[j], _list[j - 1]) < 0:
                _list[j], _list[j - 1] = _list[j - 1], _list[j]
            else:
                break
