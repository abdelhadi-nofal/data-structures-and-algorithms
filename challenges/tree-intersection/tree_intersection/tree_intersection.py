from binary_tree import BinaryTree,Node


def tree_intersection(bt1, bt2):
    bt1_values = bt1.breadth_fisrt()
    bt2_values = bt2.breadth_fisrt()
    values_in_both = []

    for value in bt2_values:
        if value in bt1_values:
            values_in_both.append(value)
    
    return values_in_both