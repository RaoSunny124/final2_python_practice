#built in function
# li = [1,2,3]
# print(sum(li))


#user_defined function
# def even_odd (x):
#     if x % 2 == 0:
#         print('it even')
#     else:
#         print('it odd')   


# user_input = int(input('Enter your number:'))  
# even_odd(user_input)  

# def fun():
#     print('welcome to GF')

# fun()  


# #parameters (variables)
# def sum(a,b):
#     print(a+b)
# #Arguments (variables)
# sum(2,3)    

# def sum(a,b):
#    return(a+b)
   
# print(sum(2,3))


# def sum(a,b):
#     z = a+b
#     print(z)
#     z += 1
#     return z
   
# print(sum(2,3))


#default
# def add(x,y=2):
#     z = x+y
#     return z

# num1 = int(input('Number1:')) 
# num2 = int(input('Number2:'))

# print(add(num1 , num2))


#positinal and keyword
# def intro(name , age):
#     print(f'my name is {name} and my age is {age}.')

# intro('Hassan', 19)   

#arbitary(args)  non-keyword arbitary
# def add(*args):
#     return sum(args)

# print(add(1 , 5 ,6))

#keyword arbitary
# def add(**a):
#     for x , y in a.items():
#         print(f'{x} = {y}')

# print(add(a = 1 , b = 5 ,c = 6))

#lamda
# add = lambda x ,y : x + y
# print(add(1,2))

# add = lambda x  : x**2
# print(add(6))

#Doc string
# def even_odd (x):
#     """its doc"""
#     if x % 2 == 0:
#         print('it even')
#     else:
#         print('it odd') 

# print(even_odd.__doc__)



def reverse_string():
    user_input = input('string:')
    reverse = user_input[::-1]
    print(reverse)

reverse_string()