#List is ordered sequence of objects.Its denoted in [].
       #Ex: [1,2,3,4,5,6],['a','b','c',TRUE]

list = [ 'prasanna', 786 , 2.23, 'kunal', 70.2 ] 
tinylist = [123, 'arjun'] 
print (list)          # Prints complete list 
print (list[0])       # Prints first element of the list 
print (list[1:3])     # Prints elements starting from 2nd till 3rd  
print (list[2:])      # Prints elements starting from 3rd element 
print (tinylist * 2)  # Prints list two times 
print (list + tinylist) #Prints concatenated lists 
print(end="\n\n\n\n\n")

print('*****Example2******',end='\n\n\n')
cart= ['grapes','toys','books','specs']

cart[0]='laptop'
#[index:index] gives [index_item:index_item]
print(cart[0::2],end='\n\n')

new_cart=cart[:]
new_cart[0]='gum'
print(new_cart,end='\n\n') 
print(cart,end='\n\n\n\n\n\n\n\n\n')





print('*******Matrix*********')
matrix=[
        [1,4,2,5],
        [2,3,6,5],
        [4,5,6,0]
       ]
print(matrix,end='\n\n')
print('Element from 0th row 1th column:')
print(matrix[0][1])
