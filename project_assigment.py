# joke_bot(1)
# def joke():
#     user_input : str = input('What do u want:')
#     joke : str = "I'll meet you at the corner!😄"
#     sorry :str = 'Sorry , I only tell one joke.'
#     if user_input.lower() == 'joke':
#         print(joke)
#     else:
#         print(sorry) 


# joke()


#double_it(2)
# def number_double():
#     user_input = int(input('Enter a number:'))
#     if user_input >= 100:
#         print('Your number is incorrect.')
#     else:
#         while user_input <= 100:
#          user_input = user_input*2
#          print(user_input , end=" ")
#     print('number is higher than 100')


# number_double()


#lift_off(3)
# def lift_off():
#     for i in range(10, 0, -1):
#         print(i , end=" ")
#     print('Liftoff🚀')

# lift_off() 

#Guessed number(4)
# def guess_game ():
#     import random
    
#     guess_my_num = random.randint(0 , 100)
#     # print('Guessed number is' , guess_my_num) 
#     user_input = int(input('Enter a number:')) 
#     if user_input > guess_my_num:
#         print('User number is too high.')
#     elif user_input < guess_my_num:
#         print('User number is too low.')
#     elif user_input == guess_my_num:
#         print(' Congrats! 🏆 The number was:' , guess_my_num)
#     else:
#         print('invalid syntax.')               
#     print('Guessed number is:' , guess_my_num)

# guess_game()  



#random_number(5)
# def random_number():
#     from random import randint

#     for x in range(1 , 11):
#         random_number = randint(1 , 101)
#         print(random_number , end=" ")

# random_number()        


# from random import randint


# user_num = randint(1 , 101)
# print(f'My user number is : {user_num}')
# computer_num = randint(1 , 101)
# print(f'Computer number is : {computer_num}')
# guess_input = input("What do u think your number is higher/lower than a computer:")
# while guess_input :
#     if guess_input == 'Higher'.lower():
#         print(f'Your number {user_num} is High.') 
#     elif guess_input == 'Lower'.lower():
#         print(f'Your number {user_num} is Low.')
#     computer_num = randint(1 , 101)
#     print(f'Computer number is : {computer_num}')

print("Welcome to the High-Low Game!\n-----------------------------")


from random import randint

score = 0
count = 0
while count < 5: 
    
    user_num = randint(1 , 101)
    print(f'Your number is : {user_num}')
    computer_num = randint(1 , 101)   
    user_guess = input("What do u think your number is higher/lower than a computer?:").strip().lower()
    computer_num = randint(1 , 101)
    print(f'Computer number is : {computer_num}')
    count += 1
    if user_guess == 'Higher'.lower():
        if user_num > computer_num:
            print(f'You were right! The computer number was {computer_num}.') 
            score = score+1 
        else:
            print("You are wrong, the computer's number is higher." , computer_num)  
    elif user_guess == 'Lower'.lower():
        if user_num < computer_num:
            print(f'You were right! The computer number was {computer_num}.')
            score += 1
        else:    
            print("You are wrong, the computer's number is lower.", computer_num) 
    print(f'Your score is now {score}.')        
# # print(f'Computer number is : {computer_num}')

class