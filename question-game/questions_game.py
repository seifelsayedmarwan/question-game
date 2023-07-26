import termcolor
"""
It is a game that gives the user the advantage of choosing the type of questions,
 and it has several types, and each type has several levels, 
 perhaps one or more
"""
termcolor.cprint("Welcme", "green")
name = print("Hello,", input("What is your name? ").capitalize())
print("Welcome to questions Game")

print("""There are three types of questions,which are 
      1- Cultural Questions,
      2- Sports Questions,
      3- Account questions """)
try:
 choose_number = int(input("Chose a number from one to three to specify the type of questions you will answer: "))
except ValueError:
    termcolor.cprint("You did not choose a number", "red")

if choose_number == 1:
    print("You chose cultural qustions")
    print("This part of the questions consists of one level")
    start = input("To get started, type start: ").lower()
    if start == "start":
       print("                                          (play page)")
       termcolor.cprint("""The answers to the questions will be in the form of choices, 
       and you have to know the correct answer 
       and write the answer number""", "yellow")
       score = 0
       #1
       chose_answer = int(input("""Which of these countries is the famous country for the Great Wall? 
       1- Egypt
       2- China
       3- Russia
       4- Vitnam:\nanswer: """
                                  ))
      
       if chose_answer != 2:
        termcolor.cprint("wrong answer", "red")
       else:
        termcolor.cprint("correct answer", "green")
        score += 1

        #2
        chose_answer = int(input("""What is the largest continent by land area? 
        1- Asia
        2- Russia
        3- Brazil
        4- America\nanswer: """
                                 ))
        if chose_answer != 1:
          termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #3
        chose_answer = int(input("""What is the capital city of Australia? 
        1- Paris
        2- Sydney
        3- Canberra
        4- Melbourne\nanswer: """
                                 ))
        if chose_answer != 3:
          termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #4
        chose_answer = int(input("""What is the largest planet in our solar system?
        1- Earth
        2- Jupiter
        3- Mercury
        4- Neptune\nanswer: """
                                 ))
        if chose_answer != 2:
          termcolor.cprint("wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #5
        chose_answer = int(input("""What is the currency of Japan?
        1- YEN
        2- EURO
        3- AUD
        4- CAD\nanswer: """
                                 ))
        if chose_answer != 1:
          termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #6
        chose_answer = int(input("""What is the capital city of Canada? 
        1- Canberra
        2- Ottawa
        3- Brazilia
        4- Tokyo\nanswer: """
                                 ))
        if chose_answer != 2:
          termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #7
        chose_answer = int(input("""Which country is known for producing the most coffee in the world? 
        1- Egypt
        2- Argantina
        3- England
        4- Brazil\nanswer: """
                                 ))
        if chose_answer != 4:
          termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #8
        chose_answer = int(input("""What is the executive capital of South Africa? 
        1- Cape Town
        2- Bloemfontein
        3- Pretoria
        4- South Africa\nanswer: """
                                 ))
        if chose_answer != 3:
         termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #9
        chose_answer = int(input("""What is the name of the largest moon of Saturn? 
        1- Enceladus
        2- Iapetus
        3- Rhea
        4- Titan\nanswer: """
                                 ))
        if chose_answer != 4:
          termcolor.cprint("Wrong answer", "red")
        else:
          termcolor.cprint("Correct answer", "green")
          score += 1

        #10
        chose_answer = int(input("""What is the capital city of Spain? 
        1- Spain
        2- Madrid
        3- Cape Town
        4- None of that\nanswer: """
                                 ))
        if chose_answer != 2:
          termcolor.cprint("Wrong answer", "red")
        else:
         termcolor.cprint("Correct answer", "green")
         score += 1

        print("Questions are over")
        print("Your score is ", score)
        if score >= 7:
          termcolor.cprint("Congratulations you succeeded", "green")
        else:
          termcolor.cprint("You lost", "red")
        
if choose_number == 2:
  print("You chose sports qustions")
  print("This part of the questions consists of one level")
  start = input("To get started, type start: ").lower()
  if start == "start":
       print("                                          (play page)")
       termcolor.cprint("""The answers to the questions will be in the form of choices, 
       and you have to know the correct answer 
       and write the answer number""", "yellow")
       score = 0
       #1
       chose_answer = int(input("""In which sport do athletes compete for the Stanley Cup? 
       1- ice hockey
       2- basket ball
       3- foot ball
       4- hand ball\nanswer:"""
                                ))
       if chose_answer != 1:
        termcolor.cprint("Wrong answer", "red")
       else:
        termcolor.cprint("Correct answer", "green")
        score += 1

       #2
       chose_answer = int(input("""How many players are on a basketball team? 
       1- three
       2- four
       3- five
       4- six\nanswer:"""
                                ))
       if chose_answer != 3:
         termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #3
       chose_answer = int(input("""Which sport uses a shuttlecock? 
       1- ice hockey
       2- Tennis
       3- hand ball
       4- None of that\nanswer:"""
                                ))
       if chose_answer != 4:
         termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #4
       chose_answer = int(input("""How many players are on a netball team? 
       1- seven
       2- eight
       3- nine
       4- five\nanswer:"""
                                ))
       if chose_answer != 1:
         termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #5
       chose_answer = int(input("""In which sport would you find the terms \"slam dunk\" and \"layup\"? 
       1- basket ball
       2- foot ball
       3- hand ball
       4- None of that\nanswer:"""
                                ))
       if chose_answer != 1:
         termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #6
       chose_answer = int(input("""Which sport uses a small ball and a racquet and is played inside a four-walled court? 
       1- ice hockey
       2- tennis
       3- squash
       4- None of that\nanswer:"""
                                ))
       if chose_answer != 3:
         termcolor.cprint("Wrong answer", "red")
       else:
        termcolor.cprint("Correct answer", "green");score += 1

       #7
       chose_answer = int(input("""How many players are on a volleyball team? 
       1- five
       2- six
       3- seven
       4- eight\nanswer:"""
                                ))
       if chose_answer != 2:
         termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #8
       chose_answer = int(input("""In which sport would you find a \"pitcher\" and a \"catcher\"? 
       1- foot ball
       2- basket ball
       3- base ball
       4- None of that\nanswer:"""
                                ))
       if chose_answer != 3:
        termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #9
       chose_answer = int(input("""How many players are on a team in a typical game of field hockey? 
       1- nine
       2- ten
       3- eleven
       4- twelve\nanswer"""
                                ))
       if chose_answer != 3:
        termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       #10
       chose_answer = int(input("""In which sport are yellow and red cards used to discipline players? 
       1- foot ball
       2- basket ball
       3- hand ball
       4- None of that\nanswer:"""
                                ))
       if chose_answer != 1:
         termcolor.cprint("Wrong answer", "red")
       else:
         termcolor.cprint("Correct answer", "green")
         score += 1

       print("Questions are over")
       print("Your score is", score)
       if score >= 7:
         termcolor.cprint("Congratulations you succeeded")
       else:
         termcolor.cprint("You lose", "red")

if choose_number == 3:
  print("You chose Account questions")
  print("This part of the questions consists of one level")
  start = input("To get started, type start: ").lower()
  if start == "start":
    print("                                          (play page)")
    termcolor.cprint("""The answers to the questions will be in the form of choices, 
       and you have to know the correct answer 
       and write the answer number""", "yellow")
    score = 0
    #1
    chose_answer = int(input("""What is the product of 7 × 8?
    1- 55
    2- 50
    3- 56
    4- 57\nanswer:"""
                             ))
    if chose_answer == 3:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")
     
    #2
    chose_answer = int(input("""What is the numerical result of the expression 12 ÷ 4?
    1- 4
    2- 3
    3- 5
    4- 6\nanswer:"""
                             ))
    if chose_answer == 2:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")

    #3
    chose_answer = int(input("""Calculate the numerical value of the expression 3² + 4 × 5 + 6:
    1- 35
    2- 25
    3- 33
    4- 36\nanswer:"""
                              ))
    if chose_answer == 1:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")
    
    #4
    chose_answer = int(input("""What is the sum of even numbers between 1 and 10?
    1- 21
    2- 30
    3- 20
    4- 19\nanswer:"""
                             ))
    if chose_answer == 3:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")

    #5
    chose_answer = int(input("""Calculate the square root of the number 144:
    1- 11
    2- 12
    3- 13
    4- 14\nanswer:"""
                             ))
    if chose_answer == 2:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")
    
    #6
    chose_answer = int(input("""What is the number that, when divided by 7, results in 3?
    1- 19
    2- 20
    3- 21
    4- 22\nanswer:"""
                             ))
    if chose_answer == 3:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")

    #7
    chose_answer = int(input("""Calculate the arithmetic mean of the numbers 15, 20, 25, 30, and 35:
    1- 22
    2- 23
    3- 24
    4- 25\nanswer:"""
                             ))
    if chose_answer == 4:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")

    #8
    chose_answer = int(input("""What is the absolute value of the number -7?
    1- (-7)
    2- 7
    3- 1
    4- 0\nanswer:"""
                             ))
    if chose_answer == 2:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")
    
    #9
    chose_answer = int(input("""Calculate the sum of odd numbers between 1 and 20:
    1- 97
    2- 98
    3- 99
    4- 100\nanswer:"""
                             ))
    if chose_answer == 3:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")
    
    #10
    chose_answer = int(input("""What is the product of multiplying 5 by 77?
    1- 385
    2- 386
    3- 387
    4- 388\nanswer:"""
                             ))
    if chose_answer == 1:
      termcolor.cprint("Correct answer", "green")
      score += 1
    else:
      termcolor.cprint("Wrong answer", "red")

    print("Questions are over")
    print("Your score is", score)
    if score >= 7:
      termcolor.cprint("Congratulations you succeeded", "green")
    else:
      termcolor.cprint("You lost", "red")

    
    
        
    