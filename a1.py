from binarytree import Node
root=Node(1)
root.left=Node(2)
root.right=Node(3)

root.left=Node(4)
root.right=Node(5)

root.left=Node(6)
root.right=Node(7)

print("Binary Tree Structure:")
print(root)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node: 
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        print(node.value, end=' ')

print("\nIn-order Traversal:")
in_order_traversal(root)

print("\n")
print("\nPre-order Traversal:")
pre_order_traversal(root)

print("\n")
print("\nPost-order Traversal:")
post_order_traversal(root)
