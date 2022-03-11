"""import ast
def Reverse(arr):
    arr.reverse()
    return arr

def Deletion(arr):
    arr.pop(0)
    return arr
T=int(input())
for i in range(T):
    arr=[]
    flow=str(input())
    n=int(input())
    arr=input()
    arr=ast.literal_eval(arr)
    for j in range(len(flow)):
        if flow[j] == "R":
            arr=Reverse(arr)
        elif flow[j] == "D":
            if len(arr) == 0:
                print("error")
                break
            else:
                arr=Deletion(arr)
    print(arr)"""
"""
import ast
import sys
input=sys.stdin.readline
def binding(arr,flow):
    for i in range(len(flow)):
        if len(arr) !=0:
            if flow[i] == "R":
                arr.reverse()
            elif flow[i] == "D":
                arr.pop(0)
        else:
            return "error"
    return arr
T=int(input())
for i in range(T):
    arr=[]
    flow=str(input())
    n=input()
    arr=input()
    arr=ast.literal_eval(arr)
    print(binding(arr,flow))
"""
"""
def deque_R(arr,Rn):
    if Rn%2 == 0:
        return arr
    else:
        arr.reverse()
        return arr

def deque_D(arr):
    if arr:
        return arr.popleft()
import sys
from collections import deque
import ast
for i in range(T):
    flow=str(input())
    n=input()
    arr=input()
    arr=ast.literal_eval(arr)
    a=deque(arr)
    print(binding(arr,flow))

print(a)
"""
import ast
import sys
from _collections import deque
input=sys.stdin.readline
def binding(arr,flow):
    for i in range(len(flow)):
        if len(arr) !=0:
            if flow[i] == "R":
                arr.reverse()
            elif flow[i] == "D":
                arr.pop(0)
        else:
            return "error"
    return (',').join(arr.split(','))
T=int(input())
for i in range(T):
    arr=[]
    flow=str(input())
    n=input()
    arr=input()
    arr=ast.literal_eval(arr)
    print(arr)
    a = deque(arr)
    print(binding(arr,flow))
