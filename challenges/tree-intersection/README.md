## Problem domain

This challenge asks us to write a function that takes two strings as arguments and returns a list of the elements that both trees have in common.

## Challenge

Traverse both trees keeping track of the values in each. Return a list of the elements that they have in common.

## Code
```
def tree_intersection(bt1, bt2):
    bt1_values = bt1.breadth_fisrt()
    bt2_values = bt2.breadth_fisrt()
    values_in_both = []

    for value in bt2_values:
        if value in bt1_values:
            values_in_both.append(value)
    
    return values_in_both
```

## Approach & Efficiency

time <- O(n)
space <- O(n)
