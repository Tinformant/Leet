# Tree
## Recommended Order for Review
Recursion/Iteration
* 98 Validate Binary Search Tree
* 101 Symmetric Tree
* 110 Balanced Binary Tree
* 111 Minimum Depth of Binary Tree
* 226 Invert Binary Tree
* 114 Flatten Binary Tree to Linked List

Iterative Binary Tree Traversal
* 94 Binary Tree Inorder Traversal
* 144 Binary Tree Preorder Traversal
* 145 Binary Tree Postorder Traversal

Properties of Binary Tree Traversal
* 105 Construct Binary Tree from Preorder and Inorder Traversal
* 106 Construct Binary Tree from Inorder and Postorder Traversal

BFS/DFS
* 199 Binary Tree Right Side View
* 515 Find Largest Value in Each Tree Row
* 637 Average of Levels in Binary Tree
* 112 Path Sum
* 113 Path Sum II
* 102 Binary Tree Level Order Traversal
* 107 Binary Tree Level Order Traversal II

DO THESE TOO
* 173 Binary Search Tree Iterator
* 617 Merge Two Binary Trees
* 108 Convert Sorted Array to Binary Search Tree

TODO
* 116 Populating Next Right Pointers in Each Node
* 117 Populating Next Right Pointers in Each Node II
* 513 Find Bottom Left Tree Value
* 437 Path Sum III
* 129 Sum Root to Leaf Numbers


## Successor and Predecessor
* 510 Inorder Successor in BST II
* 285 Inorder Successor in BST
* 450 Delete Node in a BST

## Binary Tree
* Only constraint is that a binary tree has at most two children.

## Binary Search Tree
* Left child less than parent
* Right child greater than parent
* No duplicate node
* The left and right subtree each must also be a BST.

```java
class BinaryTree {
    Node root;

    BinaryTree(int key) {
        root = new Node(key);
    }
    
    class Node {
        int key;
        Node left, right;

        Node (int item) {
            key = item;
            left = right = null;
        }
    }
}
```


### Time Complexity
* Insert, remove and search: average case O(logn), worst case O(n)

## Simple Recursion
* 98 Validate Binary Search Tree
* 100 Same Tree
* 101 Symmetric Tree
* 110 Balanced Binary Tree
* 111 Minimum Depth of Binary Tree
* 112 Path Sum
* 113 Path Sum II
* 114 Flatten Binary Tree to Linked List
* 129 Sum Root to Leaf Numbers
* 235 Lowest Common Ancestor of a Binary Search Tree
* 404 Sum of Left Leaves

## Iteration instead of Recursion
* 94 Binary Tree Inorder Traversal
* 114 Flatten Binary Tree to Linked List
* 144 Binary Tree Preorder Traversal
* 145 Binary Tree Postorder Traversal
* 230 Kth Smallest Element in a BST

## Construct Tree / Traversal
* 105 Construct Binary Tree from Preorder and Inorder Traversal
* 106 Construct Binary Tree from Inorder and Postorder Traversal
* 108 Convert Sorted Array to Binary Search Tree
* 109 Convert Sorted List to Binary Search Tree
* 255 Verify Preorder Sequence in Binary Search Tree
* 230 Kth Smallest Element in a BST
* 1008 Construct Binary Search Tree from Preorder Traversal

## Search
* 102 Binary Tree Level Order Traversal
* 107 Binary Tree Level Order Traversal II
* 116 Populating Next Right Pointers in Each Node
* 117 Populating Next Right Pointers in Each Node II
* 199 Binary Tree Right Side View
* 513 Find Bottom Left Tree Value
* 515 Find Largest Value in Each Tree Row
* 637 Average of Levels in Binary Tree
* 437 Path Sum III

## Successor and Predecessor
* 510 Inorder Successor in BST II
* 285 Inorder Successor in BST
* 450 Delete Node in a BST

https://stackoverflow.com/questions/5471731/in-order-successor-in-binary-search-tree

## TODO
* 124 Binary Tree Maximum Path Sum
* 236 Lowest Common Ancestor of a Binary Tree
* 687 Longest Univalue Path













