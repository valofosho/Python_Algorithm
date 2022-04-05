"""def L(cursor):
    if cursor == -(len(ls)):
        return cursor
    else:
        cursor-=1
        return cursor
def D(cursor):
    if cursor == -1:
        return cursor
    else:
        cursor+=1
        return cursor
def B(ls,cursor):
    print(-len(ls))
    if cursor == -(len(ls)):
        return ls
    else:
        ls.remove(ls[cursor])
        return ls
def P(ls, x, cursor):
    if cursor == -1:
        ls.append(x)
    else:
        ls.insert(cursor+1,x)
    return ls

ls=['a', 'b', 'c']
cursor=-1
cnt=int(input())
for i in range(cnt):
    order=input().split()
    if "P" in order:
        ls=P(ls, order[-1], cursor)
    elif "D" in order:
        cursor=D(cursor)
    elif "L" in order:
        cursor=L(cursor)
    elif "B" in order:
        ls = B(ls,cursor)
    print(ls,cursor)
print(ls)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
    def listSize(self):
        return self.size
    def is_empty(self):
        if self.size !=0:
            return False
        else:
            return True
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur. next
            cur.next = node
"""

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self, new_data, prev_node):
        if prev_node is None:
            print("The given prev_node must in Linked List.")
            return
        else:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next=new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last=last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp.next

for i in range(1):
    print(i)





