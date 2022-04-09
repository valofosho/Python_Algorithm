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
        elif self.head.next is None:
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
        if self.head is not None:
            # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
            if self.cur is None:
                print("2")
                return
            # 커서가 리스트의 헤드에 위치하고 헤드의 앞뒤가 None인 경우
            elif self.cur == self.head and self.head.next is None and self.head.prev is None:
                self.head = None
                self.cur = None
                print("3")
                return
            #  커서가 리스트의 헤드에 위치하는 ㄱ
                
        
        
        
        
*************        
        if self.head is not None:
            # 리스트 의 첫 번째에 해당하는 경우
            if self.cur == self.head:
                self.head = None
                self.cur = None
                return
            elif self.cur == self.tail:
                self.tail.prev.next = None
                self.tail= self.tail.prev
                self.cur =self.tail
                self.cur.next = None
                return
            else:
                self.cur.prev.next = self.cur.next
                self.cur.next.prev = self.cur.prev
                self.cur = self.cur.prev
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
        if self.cur.next is not None:
            self.cur = self.cur.next
            return
    def printls(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
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