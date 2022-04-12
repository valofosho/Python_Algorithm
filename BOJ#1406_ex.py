"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.prev = None
        new_node.next = None

        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.cur = new_node
            new_node.prev = None
            print(self.head.prev)
            print("1")
            return

        # 리스트가 비어있지 않고 뒤 값이 존재하지 않는 경우
        elif self.cur is not None and self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = None
            self.cur = new_node
            print("2")
            return

        # 리스트가 비어있지 않고 앞 뒤 값이 모두 존재하는 경우
        elif self.cur is not None and self.cur.next is None:
            new_node.prev = self.cur
            self.cur.next = new_node
            new_node.next = None
            self.cur = new_node
            self.tail = new_node
            print("3")
            return

        elif self.cur is None:
            temp = self.head
            self.head = new_node
            self.head.prev = None
            self.head.next = temp
            self.cur = self.head
            print("4")
            return
        elif self.cur.next is not None:
            new_node.prev = self.cur
            new_node.next = self.cur.next
            self.cur.next = new_node
            self.cur = new_node
            self.tail = new_node
            print("5")
            return

    def delete(self):
        # 리스트가 비어있는 경우
        if self.head is None:
            print("1")
            return
        #리스트내 원소가 존재하는 경우
        elif self.head is not None:
            # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
            if self.cur is None:
                print("2")
                return
            # 커서가 리스트의 헤드에 위치하고 헤드의 앞뒤가 None인 경우
            elif self.cur == self.head and self.head.next is None and self.head.prev is None:
                self.head = None
                print(self.cur.data)
                self.cur = None
                print("3")
                return
            #  커서가 리스트의 헤드에 위치하는 경우
            elif self.cur == self.head and self.head.next is not None:
                temp_next = self.head.next
                temp_prev = self.head.prev
                self.head.prev = None
                self.head.next = temp_next.next
                self.head =temp_next
                self.cur = None
                print("4")
                return
            # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
            elif self.cur != self.head and self.cur.next is not None:
                print(self.cur.data)

                temp_prev = self.cur.prev
                temp_next = self.cur.next
                temp_prev.next = temp_next
                temp_next.prev = temp_prev
                self.cur = temp_prev
                print("5")
                return
            # 커서가 리스트의 마지막 노드에 해당하는 경우
            elif self.cur != self.head and self.cur.next is None:
                print(self.cur.data)

                temp_prev = self.cur.prev
                temp_prev.next = None
                self.cur = temp_prev
                print("6")
                return

    def left(self):
        # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
        if self.cur is None:
            #self.cur =self.cur.prev
            #print(self.cur.data)
            print("1")
            return
        # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
        elif self.cur.prev is not None:
            self.cur = self.cur.prev
            print(self.cur.data)
            print("2")
            return
        # 커서가 리스트의 헤드에 위치하는 경우
        elif self.cur == self.head:
            self.cur = self.head.prev
            print("3")
            return
        # 현재 둘 다 걸리지 않는 경우: 커서가 리스트의 헤드 앞 None 값에 위치하는 경우
    def right(self):
        # 리스트가 비어있는 경우
        if self.head is None:
            print("1")
            return
        # 커서가 리스트의 헤드에 위치하는 경우
        elif self.head is not None and self.cur == self.head:
            temp_next = self.cur.next
            self.cur = temp_next
            print("2")
            return
        # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
        elif self.head is not None and self.cur is None:
            self.cur = self.head
            print("4")
            return
        # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우:
        elif self.head is not None and self.cur != self.head and self.cur.next is not None:
            temp_next = self.cur.next
            self.cur = temp_next
            print("3")
            return

        # 커서가 리스트의 테일에 위치하는 경우:
        elif self.head is not None and self.cur != self.head and self.cur.next is None:
            print("5")
            return
    def printls(self):
        list = []
        temp = self.head
        while temp:
            list.append(temp.data)
            temp = temp.next
        print(''.join(list))
        return


import sys
input = sys.stdin.readline
ls = DLL()
m = str(input().strip())
print(m)
for i in m:
    ls.insert(i)
num = int(input())
for i in range(num):
    order = input().split()
    if order[0] == "L":
        ls.left()
    elif order[0] == "D":
        ls.right()
    elif order[0] == "B":
        ls.delete()
    elif "P" in order:
        ls.insert(order[1])
ls.printls()






##############
##############
##############
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


# insert 의 종류
# 1. 리스트가 비어있는 경우
# 2. 리스트가 비어있지 않고, 뒤 값이 존재하지 않는 경우
# 3. 리스트가 비어있지 않고, 앞 뒤 값이 모두 존재하는 경우
# 4. 리스트가 비어있지 않고, 앞 값이 존재하지 않는 경우

# left 의 종류
# 1. 커서가 리스트의 헤드에 위치하는 경우
# 2. 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
# 3. 커서가 리스트의 헤드 전 None 값에 위치하는 경우

# right 의 종류
# 1. 리스트가 비어있는 경우
# 2. 커서가 리스트의 헤드에 위치하는 경우
# 3. 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
# 4. 커서가 리스트의 헤드 전 None 값에 위치하는 경우
# 5. 커서가 리스트의 테일에 해당하는 경우



# delete 의 종류 (delete 는 해당 노드 제거)
# 1. 리스트가 비어있는 경우 (빈 리스트)
# 2. 커서가 리스트의 헤드 전 None 값에 위치하는 경우 -> pass
# 3. 커서가 리스트의 헤드 에 위치하고 헤드의 앞뒤가 None인 경우
# 4. 커서가 리스트의 헤드에 위치하는 경우
# 5. 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
# 6. 커서가 리스트의 마지막 노드에 해당하는 경우
"""


import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.prev = None
        new_node.next = None

        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.cur = new_node
            new_node.prev = None
            return 0

        # 리스트가 비어있지 않고 뒤 값이 존재하지 않는 경우
        elif self.cur is not None and self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = None
            self.cur = new_node
            return 0

        # 리스트가 비어있지 않고 앞 뒤 값이 모두 존재하는 경우
        elif self.cur is not None and self.cur.next is None:
            new_node.prev = self.cur
            self.cur.next = new_node
            new_node.next = None
            self.cur = new_node
            self.tail = new_node
            return 0

        elif self.cur is None:
            temp = self.head
            self.head = new_node
            self.head.prev = None
            self.head.next = temp
            self.cur = self.head
            return 0
        elif self.cur.next is not None:
            new_node.prev = self.cur
            new_node.next = self.cur.next
            self.cur.next = new_node
            self.cur = new_node
            self.tail = new_node
            return 0

    def delete(self):
        # 리스트가 비어있는 경우
        if self.head is None:
            return
        # 리스트내 원소가 존재하는 경우
        elif self.head is not None:
            # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
            if self.cur is None:
                return 0
            # 커서가 리스트의 헤드에 위치하고 헤드의 앞뒤가 None인 경우
            elif self.cur == self.head and self.head.next is None and self.head.prev is None:
                self.head = None
                self.cur = None
                return 0
            #  커서가 리스트의 헤드에 위치하는 경우
            elif self.cur == self.head and self.head.next is not None:
                temp_next = self.head.next
                self.head.prev = None
                self.head.next = temp_next.next
                self.head = temp_next
                self.cur = None
                return 0
            # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
            elif self.cur != self.head and self.cur.next is not None:
                temp_prev = self.cur.prev
                temp_next = self.cur.next
                temp_prev.next = temp_next
                temp_next.prev = temp_prev
                self.cur = temp_prev
                return 0
            # 커서가 리스트의 마지막 노드에 해당하는 경우
            elif self.cur != self.head and self.cur.next is None:
                temp_prev = self.cur.prev
                temp_prev.next = None
                self.cur = temp_prev
                return 0

    def left(self):
        # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
        if self.cur is None:
            # self.cur =self.cur.prev
            # print(self.cur.data)
            return 0
        # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
        elif self.cur.prev is not None:
            self.cur = self.cur.prev
            return 0
        # 커서가 리스트의 헤드에 위치하는 경우
        elif self.cur == self.head:
            self.cur = self.head.prev
            return 0
        # 현재 둘 다 걸리지 않는 경우: 커서가 리스트의 헤드 앞 None 값에 위치하는 경우

    def right(self):
        # 리스트가 비어있는 경우
        if self.head is None:
            return 0
        # 커서가 리스트의 헤드에 위치하는 경우
        elif self.head is not None and self.cur == self.head:
            temp_next = self.cur.next
            self.cur = temp_next
            return 0
        # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
        elif self.head is not None and self.cur is None:
            self.cur = self.head
            return 0
        # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우:
        elif self.head is not None and self.cur != self.head and self.cur.next is not None:
            temp_next = self.cur.next
            self.cur = temp_next
            return 0

        # 커서가 리스트의 테일에 위치하는 경우:
        elif self.head is not None and self.cur != self.head and self.cur.next is None:
            return 0

    def printls(self,list):
        temp = self.head
        while temp:
            list.append(temp.data)
            temp = temp.next
        print(''.join(list))
        return 0



input = sys.stdin.readline
ls = DLL()
list = []
m = str(input().strip())
for i in m:
    ls.insert(i)
num = int(input())
for i in range(num):
    order = input().split()
    if order[0] == "L":
        ls.left()
    elif order[0] == "D":
        ls.right()
    elif order[0] == "B":
        ls.delete()
    elif "P" in order:
        ls.insert(order[1])
ls.printls(list)
