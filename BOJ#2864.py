#BOJ2864 5와 6의 차이
N,M=map(str,input().split())
min=int(N.replace('6','5'))+int(M.replace('6','5'))
max=int(N.replace('5','6'))+int(M.replace('5','6'))
print(min, max)
