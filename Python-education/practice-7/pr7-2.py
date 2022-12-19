n = [int(i) for i in input().split()] 
x = int(input()) 
r = [n[::-1][i] * x ** i for i in range(len(n))] 
print(sum(r))