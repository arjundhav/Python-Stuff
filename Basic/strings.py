#string operations
print('String Slicing')

#for long string use (''')
s= '''
  WOW
  0 0
  ___                    
  '''
print(s)  

print(type('Hello'),end='\n\n')

print('Hello ' + 'Arjun',end='\n\n' )

#Type Conversion 
print(type(str(int(100))))  #converting int 100 into string
print(type(int(str(100)))) #converting string 100 into int
print(end='\n\n')
#formatted strings
name= 'Aj'
age=21

print(f'Hi {name}. You are {age} years old',end='\n\n')
#Normal method-print ('hi '+ name +'. You are '+ str(age)+' years old')

#String Indexing

op='0123456789'
   #012345678910
#[start:stop:stepover]
print(f'We get all items: {op[0:10]}',end='\n\n')
print(f'We get every second element: {op[0:9:2]}',end='\n\n') #02468
print(f'We get items starting from index 1: {op[1:]}',end='\n\n')  #123456789
print(f'We get items upto index 5: {op[:5]}',end='\n\n')  #0124
print(f'We get elements at gap of 1: {op[::1]}',end='\n\n')  #0123456789
print(f'We get last item of string: {op[-1]}',end='\n\n') #negative index start from end i.e 9 here

#reversing string
print(f'It reverses the string: {op[::-1]}',end='\n\n')  #9874563210

#Methods of String
kj='Hello Arjun'

print(f'We get string in Uppercase: {kj.upper()}',end='\n\n')

print(f'We get Arjun replaced by Kunal: {kj.replace("Arjun","Kunal")}',end='\n\n')

print(f'It finds the occurance of letter "u" in string: {kj.find("u")}',end='\n\n')
