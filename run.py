#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


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
    """
    >>> alice = Person("Alice Smith", 30, 75000.00)
    >>> bob = Person("Bob Johnson", 45, 92500.50)
    """

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


if __name__ == "__main__":
    import doctest

    doctest.testmod()
