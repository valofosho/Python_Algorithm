arr=[1,2,3,4]
arr_in=[4,3,2,1]
arr_flow=[]
temp_=[]
push_cnt=0
pop_cnt=0
for i in arr_in:
    for j in arr:
        if j <=arr:
            temp_.append(j)
            arr.remove(j)
        elif




"""
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


"""