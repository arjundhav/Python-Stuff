def gcd(a, b): 
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b) 
  
a = 12
b = 8
  
# prints 12 
print("The gcd of 12 and 8 is : ", end="") 
print(gcd(12,8)) 