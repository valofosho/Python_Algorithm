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
            print("insert_1")
            return

        # 리스트가 비어있지 않고 뒤 값이 존재하지 않는 경우
        elif self.cur is not None and self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = None
            self.cur = new_node
            print("insert_2")
            return

        # 리스트가 비어있지 않고 앞 뒤 값이 모두 존재하는 경우
        elif self.cur is not None and self.cur.next is None:
            new_node.prev = self.cur
            self.cur.next = new_node
            new_node.next = None
            self.cur = new_node
            self.tail = new_node
            print("insert_3")
            return

        elif self.cur is None:
            temp = self.head
            self.head = new_node
            self.head.prev = None
            self.head.next = temp
            self.cur = self.head
            print("insert_4")
            return
        elif self.cur.next is not None:
            new_node.prev = self.cur
            new_node.next = self.cur.next
            self.cur.next = new_node
            self.cur = new_node
            self.tail = new_node
            print("insert_5")
            return

    def delete(self):
        # 리스트가 비어있는 경우
        if self.head is None:
            print("delete_1")
            return
        # 리스트내 원소가 존재하는 경우
        elif self.head is not None:
            # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
            if self.cur is None:
                print("delete_2")
                return
            # 커서가 리스트의 헤드에 위치하고 헤드의 앞뒤가 None인 경우
            elif self.cur == self.head and self.head.next is None and self.head.prev is None:
                self.head = None
                self.cur = None
                print("delete_3")
                return
            #  커서가 리스트의 헤드에 위치하는 경우
            elif self.cur == self.head and self.head.next is not None:
                temp_next = self.head.next
                self.head.prev = None
                self.head.next = temp_next.next
                self.head = temp_next
                self.cur = None
                print("delete_4")
                return
            # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
            elif self.cur != self.head and self.cur.next is not None:
                temp_prev = self.cur.prev
                temp_next = self.cur.next
                temp_prev.next = temp_next
                temp_next.prev = temp_prev
                self.cur = temp_prev
                print("delete_5")
                return
            # 커서가 리스트의 마지막 노드에 해당하는 경우
            elif self.cur != self.head and self.cur.next is None:
                temp_prev = self.cur.prev
                temp_prev.next = None
                self.cur = temp_prev
                print("delete_6")
                return

    def left(self):
        # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
        if self.cur is None:
            print("left_1")
            return
        # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우
        elif self.cur.prev is not None:
            self.cur = self.cur.prev
            print("left_2")
            return
        # 커서가 리스트의 헤드에 위치하는 경우
        elif self.cur == self.head:
            self.cur = self.head.prev
            print("left_3")
            return
        # 현재 둘 다 걸리지 않는 경우: 커서가 리스트의 헤드 앞 None 값에 위치하는 경우

    def right(self):
        # 리스트가 비어있는 경우
        if self.head is None:
            print("right_1")
            return
        # 커서가 리스트의 헤드에 위치하는 경우
        elif self.head is not None and self.cur == self.head:
            temp_next = self.cur.next
            self.cur = temp_next
            print("right_2")
            return
        # 커서가 리스트의 헤드 전 None 값에 위치하는 경우
        elif self.head is not None and self.cur is None:
            self.cur = self.head
            print("right_3")
            return
        # 커서가 헤드가 아닌 리스트의 중간에 위치하는 경우:
        elif self.head is not None and self.cur != self.head and self.cur.next is not None:
            temp_next = self.cur.next
            self.cur = temp_next
            print("right_4")
            return

        # 커서가 리스트의 테일에 위치하는 경우:
        elif self.head is not None and self.cur != self.head and self.cur.next is None:
            print("right_5")
            return

    def printls(self):
        list = []
        temp = self.head
        while temp:
            list.append(temp.data)
            temp = temp.next
        print(''.join(list))
        return



input = sys.stdin.readline
ls = DLL()
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
ls.printls()
