def tapis(n):
    print("+"+"-"*(n+1)+"+")
    for i in range(n+1):
        if i == 0:
            print("|"+"#"*(n)+" "+"|")
        elif i == n:
            print("|"+" "+"#"*(n)+"|")
        else:
               print("|"+"#"*(n-i)+" "+"#"*i+"|") 
    print("+"+"-"*(n+1)+"+")


tapis(10)    
    
    