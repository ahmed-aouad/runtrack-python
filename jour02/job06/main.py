for N in range (1,1001):
    i=2
    while i*i <= N and N % i !=0:
        i= i + 1
    if i*i > N and N > 1:
        print(N)    


