import random
score = 10
randim_number = random.randint(1,10)

while True:
    usernumebrInput = int(input('Guess : '))

    if usernumebrInput == randim_number:
       print("congratulation you guess it right! your score is " + str(score))  
       break 
    else:
       print("Kindly try again")
    score -=1