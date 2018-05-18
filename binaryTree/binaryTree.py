"""
Python 3
Binary Tree Example
1. pre - pre-order traversal recursively
2. pre2 - another recursive pre-order traversal
3. preIt - pre-order traversal Iteratively using Depth Breadth Search
4. inord - in-order traversal recursively
5. inIt - in-order traversal iteratively
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
    @param: a binary tree node
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
    @param: root - a binary tree node 
            order - start with an empty list, ends at return
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
    @param: a binary tree node
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

def inord(root):
    """
    In-order Traversal Recursively
    left, root, right
        * some time can be saved by passing list instead of adding it continuously
    @param: a binary tree node
    @return: a list
    """
    order = []

    if root:
        order += inord(root.getLeftChild())
        order.append(root.getVal())
        order += inord(root.getRightChild())

    return order


def inIt(root):
    """
    In-order Traversal Iteratively - with a stack
        * if not using a stack, the root must be stored in a temp variable
        ** cannot go up tree. Point to children only
    left, root, right
    @param: a binary tree node
    @return: a list
    """
    order = []
    if not root:
        return order

    stack = []
    node = root
    while stack or node: #empty stack = false. keep going while nodes exist
        
        while node:
            stack.append(node) # add root
            node = node.getLeftChild() # find left-most node

        #pop off most left non-visited node
        node = stack.pop()
        order.append(node.getVal())

        #check for right child
        node = node.getRightChild()


    return order

def post(root):
    """
    Post-order Traversal Recursively
    left, right, root
        * some time can be saved by passing list instead of adding it continuously
    @param: a binary tree node
    @return: a list
    """
    order = []

    if root:
        order += post(root.getLeftChild())
        order += post(root.getRightChild())
        order.append(root.getVal())

    return order


def postIt(root):
    """
    In-order Traversal Iteratively - with a stack
        * if not using a stack, the root must be stored in a temp variable
        ** cannot go up tree. Point to children only
    left, right, root
    @param: a binary tree node
    @return: a list
    """
    def peak(stack):
        """
        next node in the stack. False if stack is empty
        """
        if len(stack) > 0:
            return stack[-1]
        return None

    def isLeaf(node):
        """
        is the node childless?
        """
        if (node.getLeftChild() is None) and (node.getRightChild() is None):
            return True
        return False 

    def ascending(node, last):
        """
        Were either children recently visitied? Going up the tree if True.
        """
        if node.getRightChild() and node.getRightChild() == last:
            return True
        elif node.getLeftChild() and node.getLeftChild() == last:
            return True
        return False

    order = []
    stack = [root]
    last = None
    node = root

    while stack:

        if isLeaf(node) or ascending(node, last):
            last = stack.pop()
            order.append(node.getVal())
            node = peak(stack)

        else:
            # no left child
            if node.getRightChild() and not node.getLeftChild():
                stack.append(node.getRightChild()) 
                node = node.getRightChild()

            # both children
            elif node.getLeftChild() and node.getRightChild(): 
                stack.append(node.getRightChild())
                stack.append(node.getLeftChild())
                node = node.getLeftChild()

            #no right child
            else:
                stack.append(node.getLeftChild())
                node = node.getLeftChild()

    return order


def main():
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node3.setLeftChild(node1)
    node3.setRightChild(node4)
    node1.setLeftChild(node0)
    node1.setRightChild(node2)
    node4.setRightChild(node5)

    print(postIt(node3))

main()


