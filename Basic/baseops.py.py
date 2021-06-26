print('welcome User \n')

name=input('Enter Name: ')
print(name)
print(type(name))

print('adding nos')
x=12+14
print(x)

print('dividing nos')
y=x/2
print(y)
print(type(y))

z=input("enter value of z:")
p=int(x)+(int(y)/int(z))
print(p)

p+=3
print(f'new value of {p}')

#additional operations
print(2 ** 3)             #exponential
print(5 // 4)             #quotient
print(6 % 4)              #modulo(remainder)

#math function
print(round(4.9))
print(abs(-50))
print(bin(5))            #decimal to binary conversion
print(int('0b101',2))   #binary to decimal

#operator precedence
print(20-3*4) #precedence * -> -
print((20-3)+2 ** 2) 
print('Thanks for Joining')
