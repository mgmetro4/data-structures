"""
Python 3
Binary Tree Example
"""

class Node():
    """
    Binary Tree Node
    @param: val - data payload
            leftChild - left child node
            rightChild - right child node
    """
    def __init__(self, val, leftChild=None, rightChild=None):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild

    def setVal(self, newVal):
        self.val = newVal

    def getVal(self):
        return self.val

    def setLeftChild(self, node):
        self.leftChild = node

    def setRightChild(self, node):
        self.rightChild = node

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild


def pre(root):
    """
    Pre-order Traversal Recursively
    root, left child, right child
    @return: a list
    """
    order = []
    if root:
        order.append(root.getVal())
        order += pre(root.getLeftChild())
        order += pre(root.getRightChild())

    return order


def pre2(root, order):
    """
    Another example of Pre-order Traversal Recursively
    root, left child, right child
    @param: order - start with an empty list, ends at return
    @return: a list
    """
    if not root:
        return

    order.append(root.getVal())
    pre2(root.getLeftChild(), order)
    pre2(root.getRightChild(), order)

    return order


def preIt(root):
    """
    Pre-order Traversal Iteratively - Depth Breadth Search with a Stack
    root, left child, right child
    @return: a list
    """
    order = []
    stack = [root]
    if not root:
        return order

    while stack:
        node = stack.pop()
        order.append(node.getVal())

        #add right child first so left child will get popped off the stack next
        if node.getRightChild(): stack.append(node.getRightChild())
        if node.getLeftChild(): stack.append(node.getLeftChild())

    return order


def main():
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node3.setLeftChild(node2)
    node3.setRightChild(node4)
    node2.setLeftChild(node0)
    node2.setRightChild(node1)
    node4.setRightChild(node5)

    print(preGen(node3))

main()


