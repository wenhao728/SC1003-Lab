import random

WIDTH = 4

numList = [1,2,3,4,5,6,7,8,9,0]


############################################################ 
# # functionality: randomly generate the target number 
# # input:
# #     numList: the list with 10 digits 
# #     count: the number of digits to generate 
# # output: a list with four digits (integers)

def genNumbers(numList, count):
    ## TODO ## 
    # ## Shuffle the numList and return the shuffled list
    numbers = random.sample(numList, k=count)
    # numbers = [3, 5, 9, 6]

    return numbers 


############################################################

############################################################ 
# # functionality: obtain the guessing from users
# input: None # output: a list with four digits (integers)

def userGuess():

    inputStr = input("Please input 4 digits: ")

    ## TODO ## 
    # ## Check user input and ensure user entered correct 
    # ## datatype and length of input.

    while len(inputStr) != 4:
        print("Wrong format. Please enter 4 digits.")
        inputStr = input("Please input 4 digits: ")

    guess = []

    ## TODO ## 
    # ## Transfer the user input to guess list.
    for i in range(len(inputStr)):
        try:
            guess.append(int(inputStr[i]))
        except Exception as e:
            raise ValueError(f"Please enter digits only. {e}")

    return guess 


############################################################

############################################################ 
# # functionality: compare the user guessing with the target 
# # input:
# #     guessList: the list of four digits (user guessing) 
# #     answerList: the list of four digits (target) 
# # output: a tuple (#A, #B)

def checkGuess(guessList, answerList):

    ## TODO ## 
    # ## Check how many correct number entered by the user 
    # ## and return the count (bulls, cows).
    bulls = 0
    cows = 0

    for i in range(len(guessList)):
        if guessList[i] == answerList[i]:
            bulls += 1
        elif guessList[i] in answerList:
            cows += 1

    return (bulls, cows) 


############################################################

############################################################ 
# # Main program putting all function together

answer = genNumbers(numList, WIDTH) 
# print(answer) ## UNCOMMENT THIS TO SEE WHAT WAS THE ## SHUFFLED LIST

attemps = 0

while True:

    guesses = userGuess() 
    attemps += 1 
    # print(guesses)

    result = checkGuess(guesses, answer) 
    # print(result)

    if result[0] == 4:
        print("You Win!!") 
        print("Attemps: ", attemps) 
        break

    else:
        print(result[0], "A (Bulls)", result[1], "B (Cows)")