
import sys
input=sys.stdin.readline
N=int(input())
ls, stack, temp, flow= [], [], [], []
cnt_pop, cnt_push= 0, 0
for i in range(N):
    stack.append(int(input())) #입력값 stack에 적립
    ls.append(i+1)
ls.sort(reverse=True)
for i in range(N):
    if stack[i] > ls[-1]:
        temp.append(ls[-1])
        ls.remove(ls[-1])
        flow.append('push')
    elif stack[i] == ls[-1]:
        temp.append(ls[-1])
        ls.remove(ls[-1])
        flow.append('push')
        temp.remove(ls[-1])
        flow.append('pop')


"""
초기에 빈 리스트가 있는 경우 + pop 연산으로 인해 빈 리스트로 회귀하는 경우
초기의 빈 리스트는 맹목적인 appending이 가능하나 
pop 연산으로 연산된 빈 리스트에 맹목적인 appending은 불가능하다.
+ stack에서의 인덱스와 정수형 i 변수를 같은 변수로 취급하는 경우 문제 발생
+ 예를 들어, i==3, stack[i]=4일 때, 정수형 4의 값을 받게되면
+ 다음 값으로 넘어가면서 기준이 되는 stack의 인덱스에 변화가 오게 된다
+ 자 그러면 우리 머리를 써보자
+ 맞아 난 머리가 없었던 거야
+ 빈 리스트가 생기는 경우가 크게 3가지
1) 빈 스택으로 시작하는 경우
2) pop 연산으로 인해 스택 내 원소가 나간 경우
3) 마지막 pop 연산으로 인해 모든 원소가 소모된 경우
3번의 경우에는 어차피 indexing 처리하는 과정에서 OOR 에러가 발생할 가능성이 현저히 적음(거의없다)
1번의 경우 어떠한 값을 pop하는 연산을 원하는지에 상관없이 push 연산이 일어나야 한다. (1에 대한 push 연산이 확정적으로 필요함)
2번의 경우 가장 애매한 경우로 1, 3번과 동일선상에 있는 경우이지만, 현상태에서의 push연산은 가능하나 pop 연산은 불가능하다.

보통 push 연산의 경우에서 오류가 발생할 경우의 수는 존재하지 않는다.
예외처리의 경우 극단적으로 pop 연산 에서만 발생하게 되는데, 이는 끼인값 문제와 결을 함께하고 
문제에서 주어지는 입력값이 중복되어 나타나는 경우는 없기 때문에 값 크기 대조를 통해
top 값보다 작은 값을 pop 해야 하는 경우 즉 stack[i] < ls[top] 인 경우에 에러를 반환시킨다.

*****종합해보면, ls가 비어있는 경우 push 가 발생, ls[top]보다 stack[i]가 더 작은 경우 에러가 발생한다.***** 

결국 현재 문제가 되고 있는 부분은, 입력값이 아닌, 
비교를 위한 대조군을 어떠한 형식으로 설정을 하며,
리스트를 통해 설정할 경우, 리스트의 인덱스를 따로 조건, 반복문을 통해 




카운팅이 이 문제에서 의미가 없는게 단순하게 횟수를 묻는 문제가 아니기 떄문

int a,b,c;
a>b, b<c, a>c
예를 들어 3 1 2의 경우 스택으로 구현할 수 없다.
예시 1번과 같이
처음으로 나와야 하는 값이 4라면
push, push, push, push, pop 의 연산이 필요하다.
다만 이 문제의 경우 deque나 que가 아닌 stack으로의 문제로 구성되어 있다.
LIFO의 특성을 갖는 stack은 결국 오름차순의 형석을 따른다는 전제조건과 함께 생각하면
가장 큰 수를 뽑기 위해서는 그보다 작은 수들이 밑에 깔려있고 중간 값을 꺼낼 수 없다는 것
시간 복잡도 상관 없이 구현 먼저

목표로 설정한 리스트 한 값에 맞춰서 진행해야 겠지?
a[0] 이 4다.
cons[]에서 이보다 적은 수들을 스택에 적립

Stack의 가장 큰 특징에는 무엇이 있을까?
1) Stack은 LIFO의 특성을 따른다
2) Stack의 마지막 원소는 특정 배열길이를 설정하지 않은 이상 top과 동일시한다.
3) python에서의 stack의 구현은 list형으로 이루어진다.

Stack, Que, Deque, Dict, List, Tree (정리 요)

Ls-> Temp로 옮기는 state 전제
1) 현 상태의 stack[i] 값이 Temp의 top에 비해 큰 경우



"""
# 어떤 조건에서 comp를 넘겨야할까
# 만약 동일한 원소를 pop 연산 한 경우에 인덱스를 넘기면
# 다음 값에 대한 비교 연산이 이루어지는데
# 이 과정에서 만약 다음 값이 증가한 comp 값과 비교하였을 떄
# comp 값에 비해 큰 경우 또 다시 push하는 연산이 된다.
import sys
input = sys.stdin.readline
N = int(input())
s, t, f = [], [], []
for i in range(N):
    a=int(input())
    s.append(a)
comp=1
error_code=0
for idx in range(N):
    while comp <= s[idx]:
        t.append(comp)
        f.append("+")
        comp+=1
    if t[-1] == s[idx]:
        t.pop()
        f.append("-")
    else:
        print("NO")
        error_code=1
        break
if not error_code == 1:
    print('\n'.join(f))

"""    while comp <= s[idx]: # 값의 크기가 같거나 작다면 push해주는 공통점
        t.append(comp)
        f.append("+")
        comp+=1
        if t[-1] == s[idx]: # 값의 크기가 같은 경우라면 pop 해주는 연산 필요
            t.remove(t[-1])
            f.append("-") # 동일한 경우 flow 리스트에 추가
"""