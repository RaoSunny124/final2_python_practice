# def reverse_string():
#     user_input = input('string:')
#     reverse = user_input[::-1]
#     print(reverse)

# reverse_string()

name = input('Enter name:')
edu  = input('education:')
roll_no = input('rollno:')
tu = (name , edu , roll_no)
print(tu)
li = list(tu)
print(li)
li.insert(0 , 'Ali')
print(li)