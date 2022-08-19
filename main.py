print("Welcome to My Data Structure And Algorithm")
#--------------Linked List---------
#Create A node First
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

n1 = Node(2)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)
n5 = Node(90)
n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
n4.nextNode = n5
def countNodes(head):
    count  = 1
    currentNode = head
    while currentNode != None :
        currentNode = currentNode.nextNode
        count += 1
    print(f"We have {count} nodes")
    return  count
print(countNodes(n1))

class LinkedNodes:
    def __init__(self):
        self.start = None

    def TraverseLinkedList(self):
        p = self.start
        if p == None:
            print("empty List")
            return
        while p != None :
            print(p.data)
            p = p.nextNode
            return p , p.data , p.nextNode

    def countNodes(self):
        p =self.start
        count = 0
        while p != None:
            count += 1
            p = p.nextNode
        print(f"There are {count} nodes in this Linked List")
        return  count

    def findValue(self, x):
        p = self.start
        position = 1
        if p == None:
            return "No List"

        while p != None:
            if p.data == x :
                break
            position = + 1
        return position


lN = LinkedNodes(n1)
print(lN.TraverseLinkedList())


# p= lN.start
# print(p.data)
# p = p.nextNode
# print(p.data)
# p = p.nextNode
# print(p.data)

















# Linear Search in Python
# def linearSearch(array, arrayLength, numberToFind):
#     # Going through array sequencially
#     for i in range(0, arrayLength):
#         if (array[i] == numberToFind):
#             return i
#     return -1
#
# def linearSearcher(array, numberToFind):
#     # Going through array sequencially
#     for i in range(0, len(array)):
#         if (array[i] == numberToFind):
#             return i
#     return -1
#
# # def linearSearh(array, numberToFind):
# #     # Going through array sequencially
# #     for i in array:
# #         if (array[i] == numberToFind):
# #             print(i)
# #             return i
# #     return -1
#
# print(linearSearcher( [2, 4, 0, 1, 9,30, 60, 70],60))
