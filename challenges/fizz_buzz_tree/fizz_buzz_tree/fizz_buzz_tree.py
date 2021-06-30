class Node:
    def __init__(self,value):
        self.value = value
        self.child = []

class K_ary_tree:
    def __init__(self,root = None):
        self.root = root

def fizz_buzz_tree(K_ary_tree):


        output = []
        
        queue = []
        queue.append(K_ary_tree.root)
        
        while queue:
            node = queue.pop(0)
            if node.value % 3 == 0 and node.value % 5 == 0:
                output += ['FizzBuzz']
            elif node.value % 3 == 0:
                output += ['Fizz']
            elif node.value % 5 == 0:
                output += ['Buzz']
            
            elif node.value % 3 != 0 and node.value != 0:
                output += str(node.value)

            for child in node.child:
                queue.append(child)

        return output


if __name__ == "__main__":

    k_tree = K_ary_tree()
    k_tree.root = Node(3)
    k_tree.root.child+=[Node(7)]
    k_tree.root.child+=[Node(6)]
    k_tree.root.child+=[Node(2)]
    k_tree.root.child+=[Node(5)]
    k_tree.root.child+=[Node(15)]
    k_tree.root.child+=[Node(5)]
    k_tree.root.child+=[Node(9)]
    k_tree.root.child+=[Node(4)]



    print(fizz_buzz_tree(k_tree))

