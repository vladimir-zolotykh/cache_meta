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
    def __init__(self):
        print("creating Spam instance")


if __name__ == "__main__":
    s1 = Spam()
    s2 = Spam()
    print(s1 is s2)
