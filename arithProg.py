#take an ap of first two integers as input
#take another input say n now we find value in ap at nth place
l=list(map(int,input().split()))
a=l[0]
b=l[1]
d=a-b
n=int(input())
output=a+(n-1)*d
print(output)
