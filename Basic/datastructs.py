#Dictionaries(unordered key-value pair) are enclosed by curly braces ({ }) and
#values can be assigned and accessed using square braces ([])
print('********DICTionAry**********',end='\n\n\n\n')
dict = {} 
dict['one'] = "This is one" 
dict[2] = "This is two" 
tinydict = {
            'name': 'john',
            'code':6734, 
            'dept': 'sales'
            #[100]: 'error'    We cant use List as key.
           } 
#print(tinydict[100])  It gives an ERROR           
print (dict['one'],'\n')       # Prints value for 'one' key 
print (dict[2],'\n')           # Prints value for 2 key 
print (tinydict,'\n')          # Prints complete dictionary 
print (tinydict.keys(),'\n')        # Prints all the keys 
print (tinydict.values(),'\n')       # Prints all the values
print('name' in tinydict.keys(),'\n')     #Checks the presence of name in keys      
bigdict= [
          {'name': 'Kunal',
           'code':6704,
           'dept': 'IT'
          }, 
          {'name': 'Arjun',
           'code':6734, 
           'dept': 'Comp'
          } 
        ]
print(bigdict[0]['name'][0],end='\n\n')

     #**************TUPLE***************

#A tuple is another sequence data type that is similar to the list.
#A tuple consists of a number of values separated by commas.
#Unlike lists, however, tuples are enclosed within parenthesis. 
print('********TUPLE**********','\n')
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) 
tinytuple = (123, 'john') 
print (tuple,'\n')           # Prints complete tuple 
print (tuple[0],'\n')        # Prints first element of the tuple 
print (tuple[1:3],'\n')      # Prints elements starting from 2nd till 3rd  
print (tuple[2:],'\n')       # Prints elements starting from 3rd element 
print (tinytuple * 2,'\n')   # Prints tuple two times 
print (tuple + tinytuple,'\n') # Prints concatenated tuple 
print(786 in tinytuple,'\n')    #checks presence of 786 in given tuple   
print(tuple.count(2),'\n')     #counts of 2 in tuple


                  #*****SETS *******

#Its stores values of same type
print('*+*+--SeTs--+*+*','\n')
mset={1,2,3,4,5}
yset={4,5,6,7,8,9,10}

print(mset.difference(yset),'\n')
print(mset.discard(4),'\n')
print(mset,'\n')
print(mset.difference_update(yset),'\n')
print(mset.intersection(yset),'\n')   #print(mset & yset,'\n')
#print(mset.disjoint(yset),'\n')
print(mset.issubset(yset),'\n')
print(yset.issuperset(mset),'\n')
print(mset.union(yset))  #print(mset | yset)
