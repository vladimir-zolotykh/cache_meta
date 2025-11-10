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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
