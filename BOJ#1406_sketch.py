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
        self.last = None
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
    # cursor의 위치를 앞 뒤로 변환해줘야 되기 때문에 double linked list 로 변환

#04/07
    # cursor 변수의 위치를 클래스 내부에서 선언 vs 외부에서 할당 변수로 선언
    # cursor 변수가 위치하는 부분에서 insertAfter 연산 (o)
    # cursor 위치가 head 에 해당하는 경우 기존의 push 연산과 동일한 연산  수행하도록

    #1) P 연산
    #P 연산은 크게 세 가지의 연산자로 나뉘게 된다.
    #1. cursor가 head 위치에 놓여있는 경우
    #2. cursor가 중간 위치에 놓여있는 경우
    #3. cursor가 마지막, 즉 cursor.next 가 None을 가르키고 있는 경우

    # cursor를 값 자체에 할당하여 사용하게 되면 문제 발생
    # cursor 가 head 에 할당되어 있을 경우 문제 발생
    # cursor의 경우 문자의 앞, 즉 헤드 앞에 위치할 수 있기 때문에
    # insertAfter을 곧바로 사용하게되면 문제 발생

    # cursor 의 위치가 맨 앞인 경우, 즉 head 에 해당하거나 head 앞에 들어가는 걸 찾아내야함


class Node(object):
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class LinkedList(object):
    def __init__(self):
        self.head = None

    def L(self, index_c):
        # list 내에 값이 비어있는 경우
        if self.head is None:
            return index_c
        # list 내에 값이 존재하는 경우
        if index_c == 0 or index_c == -1:
            index_c = -1
            return index_c
        else:
            index_c -= 1
            return index_c

    def D(self, index_c, ls):
        # List 내에 값이 비어있는 경우:
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
        if self.head is None or index_c == -1:
            new_node = Node(new_data)
            self.head = new_node
            new_node.next = self.head
            self.head = new_node
            index_c += 1
            return index_c
        # 커서가 중간부터 위치하는 경우
        index = 0
        current = self.head
        temp = self.head
        prev = self.head
        while current is not None:
            if index == index_c + 1:
                temp = current.next
                break
            prev = current
            current = current.next
        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node
        index_c += 1
        return index_c

    def B(self, index_c):
        if self.head is None:
            return
        if index_c == 0:
            self.head == self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == index_c:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    def getlength(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, new_data, prev_node):
        if prev_node is None:
            print("The given prev_node must in Linked List.")
            return
        else:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            prev.next = temp.next
        if temp == None:
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
        prev.next = temp
        return prev

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


import sys

input = sys.stdin.readline
ls = LinkedList()
ms = str(input())
for i in ms:
    ls.append(i)
num = int(input())
index_c = ls.getlength()
for i in range(num):
    order = input().split()
    if order == "L":
        index_c = ls.L(index_c)
    elif order == "D"
        index_c = ls.D(index_c, ls)
    elif order == "B":
        ls =

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