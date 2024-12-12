#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a has fewer than 2 elements, use 0 for missing elements
    a1, a2 = (tuple_a + (0, 0))[:2]
    # If tuple_b has fewer than 2 elements, use 0 for missing elements
    b1, b2 = (tuple_b + (0, 0))[:2]
    
    # Return a tuple with the sums of the corresponding elements
    return (a1 + b1, a2 + b2)
