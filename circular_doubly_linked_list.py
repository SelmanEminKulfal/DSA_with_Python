class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)
node5 = Node(5)

node1.next = node2 # type: ignore
node1.prev = node5 # type: ignore

node2.prev = node1 # type: ignore
node2.next = node3 # type: ignore

node3.prev = node2 # type: ignore
node3.next = node4 # type: ignore

node4.prev = node3 # type: ignore
node4.next = node5 # type: ignore

node5.prev = node4 # type: ignore
node5.next = node1 # type: ignore

print("\nTraversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ") # type: ignore
    currentNode = currentNode.next # type: ignore
print("...")

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ") # type: ignore
    currentNode = currentNode.prev # type: ignore
print("...")