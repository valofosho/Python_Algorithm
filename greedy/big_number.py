N,M,K = map(int,input().split())
N = list(map(int,input().split()))

ans = 0
N.sort(reverse=True)
num0 = N[0]
num1 = N[1]
cnt = 0
answer = 0
for i in range(M):
	if cnt == K:
		answer += num1
		cnt = 0
	else:
		answer += num0
		cnt += 1
print(answer)