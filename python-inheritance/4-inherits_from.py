#!/usr/bin/python3
"""
Module 4-inherits_from
Contains a function inherits_from that checks if an object is an instance of
a class.
"""
def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class
