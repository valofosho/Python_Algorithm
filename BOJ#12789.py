import sys
input=sys.stdin.readline
N=int(input())
s=list(map(int,input().split()))
c, t = [], []




"""
이번 문제의 핵심
1) 하나의 스택만을 활용하여 소스 리스트를 타겟 리스트로 sorting
2) 과연 어떠한 상태에서 sad 가 출력되어야 하는가
3) 교착 상태에 걸리게 되면 sad 가 출력된다.
    - ex) 교착상태란, 스택에 5가 쌓여있고 원천의 top이 가르키는 수가
         6이라고 생각한다면, 6은 타겟과 스택 모두에 들어갈 수 없는 상황이
          발생하게 된다.
"""