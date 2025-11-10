#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        # cls = <class '__main__.Spam'>
        if not cls.instance:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print("creating Spam instance")


if __name__ == "__main__":
    s1 = Spam()
    s2 = Spam()
    print(s1 is s2)
