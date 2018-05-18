# Data Structures

## Trees
Use: As a recursive hierarchical data structure.
Constraints: No reference can be duplicated (Two roots cannot point to the same child node). Children nodes cannot point to the root node.

Representation of data as "trees" that point to other trees (called children). Mathematically, it creates a directed acyclic graph of N nodes and N-1 edges.

Some Definitions:
  - **Node**: Every data object represented in the tree. Each node is the root of its own tree.
  - **Root**: the top node in a tree
  - **Parent**: Root pointing at given child
  - **Child**: Node pointed at by another (parent) node
  - **Siblings**: nodes with the same parent
  - **Descendant**: Node that can be reached by traversing from parent to child.
  - **Anestor**: Node that can be reached by traversing from child to parent.
  - **Leaf**: Node with no children
  - **Edge/Branch**: One way connection between one node and another that points away from the parent.
  - **Depth**: number of edges from tree's root node to current node.
  - **Height**: number of edges on the longest path between the node and a leaf.


### Binary Trees 
Trees in which each node has at most two children. Commonly referred to as left child and right child.

#### Traversal (Tree Search): the proess of visiting each node in a tree data structure exactly once.
  - **Pre-order**: root, left child, right child. Useful for re-creating a tree in hierarchical order such that the root is created first, then the left child, and lastly the right child.
  - **In-Order**: left child, root, right child. Useful for retrieving data in sorted order, e.g. from least to greatest.
  - **Post-order**: left child, right child, root. Useful for deleting nodes such that the root is deleted last.
  - **Recursive/Iterative**: