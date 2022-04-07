class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def L(self, index_c):
        # list 내에 값이 비어있는 경우
        if self.head is None:
            return index_c
        # list 내에 값이 존재하는 경우
        if index_c == 0 or index_c == -1 :
            index_c = -1
            return index_c
        else:
            index_c -= 1
            return index_c
    def D(self, index_c, ls):
        #List 내에 값이 비어있는 경우:
        if self.head is None:
            return index_c
        # index_c가 리스트 마지막에 위치하는 경우:
        if index_c == ls.getlength() - 1:
            return index_c
        else:
            index_c += 1
            return index_c

    def P(self, index_c, new_data):
        # 리스트가 비어있거나
        # 커서가 맨 앞으로 위치하는 경우
        if self.head is None:
            new_node = Node(new_data)
            self.head = new_node
            new_node.next = self.head
            self.head = new_node
            index_c += 1
            return index_c
        if index_c == -1:
            new_node = Node(new_data)
            self.head = new_node
            new_node.next = self.head
            self.head = new_node
            index_c += 1
            return index_c

        index = 0
        current = self.head
        prev = self.head
        temp = self.head

        while (current is not None):
            if index == (index_c + 1):
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        print(index, index_c)
        new_node = Node(new_data)
        new_node.next =current.next
        current.next = new_node
        index_c += 1
        return index_c

    def B(self, index_c):
        if self.head is None:
            return
        if index_c == 0:
            self.head == self.head.next
            return
        index = 0
        current =self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == index_c:
                temp = current.next
                break
            prev= current
            current = current.next
            index += 1
        prev.next = temp
        return

    def getlength(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count



    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

import sys
input =sys.stdin.readline
ls = LinkedList()
ms = str(input())
for i in ms:
    ls.append(i)
num = int(input())
index_c = ls.getlength() -1
print(index_c)
for i in range(num):
    order=input().split()
    if order == "L":
        index_c = ls.L(index_c)
    elif order == "D":
        index_c = ls.D(index_c, ls)
    elif order == "B":
        ls = ls.B(index_c)
    elif "P" in order:
        index_c = ls.P(index_c, order[1])
ls.printlist()

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