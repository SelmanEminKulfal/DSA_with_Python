class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(int(input("Type first number : ")))
node2 = Node(int(input("Type second number : ")))
node3 = Node(int(input("Type third number : ")))
node4 = Node(int(input("Type fourth number : ")))
node5 = Node(int(input("Type fifth number : ")))

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
currentNode = node5
startNode = node5
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ") # type: ignore
    currentNode = currentNode.prev # type: ignore
print("...")