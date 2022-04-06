
class Node(object):
    def __init__(self, next = None, prev = None, data = None, curs = None):
        self.next = next
        self.prev = prev
        self.data = data
        self.curs = curs
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def P(self, curs, new_data):
        if curs == self.head:




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

    def deleteNode(self, key):
        temp=self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            prev.next = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def deletebyP(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next= temp
        return prev



    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

import sys
input =sys.stdin.readline
ls = LinkedList()
ms = str(input())
for i in ms:
    ls.append(i)
num = int(input())
cur = ls
for i in range(num):
    order=input().split()

    # Linked List 에서는 index를 사용할 수 없다.
    # P 관련 method
    # 1) push(self, new_data) -> head 위치에 추가
    # 2) append(self, new_data) -> 리스트 마지막에 값 추가
    # 3) insertAfter(self, new_data, prev_node)
    # Notice
    # 1) next method는 연이어 사용할 수 없다 (ex. head.next.next 불가능)
    # 2) insertAfter method의 prev_node를 활용할 수 있는 방안은 head 만을 이용해야 한다.
    # Solve
    # 1) cur이라는 새로운 변수를 할당
    # 2) None 을 가르킬 때 까지 while문 할당
    # 3) cur 이 None 을 가르키는 의미는 List 의 마지막 값에 도달했음을 의미
    #  각 연산 별 cursor 의 연산 행동
    # 1) L: cursor의 prev 를 찾