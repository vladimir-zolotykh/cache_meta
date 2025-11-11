#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Any
import unittest


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        # cls = <class '__main__.Spam'>
        if not hasattr(cls, "_instance"):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Spam(metaclass=Singleton):
    """
    >>> s1 = Spam()
    creating Spam instance
    >>> s2 = Spam()
    >>> s1 is s2
    True
    """

    def __init__(self):
        print("creating Spam instance")


import weakref  # noqa E402


class Cache(type):
    def __call__(cls, *args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if not hasattr(cls, "_cache"):
            cls._cache = weakref.WeakValueDictionary()
        if key in cls._cache:
            instance = cls._cache[key]
        else:
            instance = super().__call__(*args, **kwargs)
            cls._cache[key] = instance
        return cls._cache[key]


class Person(metaclass=Cache):
    def __init__(self, name, age, salary):
        print(f"creating Person({name}) ...")
        self.name = name
        self.age = age
        self.salary = salary


def as_tuple(person: Person) -> tuple[Any, ...]:
    return tuple(person.__dict__.values())


class TestCache(unittest.TestCase):
    def test_10(self):
        args = "Alice Smith", 30, 75000.00
        alice = Person(*args)
        self.assertEqual(as_tuple(alice), args)

    def test_20(self):
        args = "Bob Johnson", 45, 92500.50
        bob = Person(*args)
        self.assertEqual(as_tuple(bob), args)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    unittest.main()
