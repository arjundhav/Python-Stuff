
#---------------if-else:----------------
amount=int(input("Enter amount: ")) 
if amount<=1000: 
    discount=amount*0.05 
    print ("Discount",discount) 
else: 
    discount=amount*0.10 
    print ("Discount",discount) 
     
print ("Net payable:",amount-discount,'\n\n') 



#-----------------elif-----------------------
amount=int(input("Enter amount: ")) 
 
if amount<1000: 
    discount=amount*0.05 
    print ("Discount",discount) 
elif amount<5000: 
    discount=amount*0.10 
    print ("Discount",discount) 
else: 
    discount=amount*0.15 
    print ("Discount",discount)
print ("Net payable:",amount-discount,'\n\n') 


#-----------------Nested if---------------------
num=int(input('Enter Number: '))
if num%2==0: 
    if num%3==0: 
        print ("Divisible by 3 and 2") 
    else: 
        print ("divisible by 2 not divisible by 3") 
else: 
    if num%3==0: 
        print ("divisible by 3 not divisible by 2") 
    else: 
        print  ("not Divisible by 2 not divisible by 3") 
