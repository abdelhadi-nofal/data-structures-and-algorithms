class Node:
    """
    This is the Node Class
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
       
    
    def breadth_fisrt(self):

        output = []

        queue = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            output.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not queue:
                break
        print('Output:', output)
        return output