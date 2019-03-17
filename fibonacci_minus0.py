#Question- Print the sequence 1, 1, 2, 3, 5, 8, 13, 21,...
def fibonacci(n):
  fib=[1,1]
  for i in range(2,n):
    x=fib[i-1]+fib[i-2]
    fib.append(x)
  print(*fib)
#driver code
fibonacci(10)
