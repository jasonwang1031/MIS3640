"""
# exercise 1
A = 50
B = 100

if type(A) == type("Jason") or type(B) == type("Jason"):
    print("string involved")
else:
    if A > B:
        print("bigger")
    elif A == B:
        print("equal")
    else:
        A < B
        print("smaller")


# exercise 2 question 3

def gcd(A,B):
    if A == 0:
        print(B)
    elif B == 0:
        print(A)   
    else:
        if A > B:
            result = A % B
            A = B
            B = result
            return(gcd(A,B))
    
        elif B>A:
            result = B % A
            B = A
            A = result
            return(gcd(A,B))
    
        else:
            B == A
            return(A)

print(gcd(12,12))

# question 4
def move(n,source,bridge,destination):  
    
    if n > 1:
    
        move(n-1,source,destination,bridge)  
        
        print(source,"-->", destination)  
        
        move(n-1, bridge, source, destination)  

    else:

        print(source,'-->', destination)

move(3,'A','B','C')  
