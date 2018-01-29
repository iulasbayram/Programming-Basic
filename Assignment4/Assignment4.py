#Student Name: Ismail Ulas Bayram
#Student ID: 220201040

import random

print "A game according to you. Welcome!"

user_name = raw_input("What is your name ?\n")
print
print "Soon, your word will be selected ! " + user_name

words = ['stack', 'queue', 'tree', 'linked list', \
         'software', 'hardware', 'operating systems',\
         'algorithm', 'computer', 'network']

# Below that, first of all, i wrote import of "random.choice" but after, when program does not synchronize, and
#  i used to import of "random.randint"
def random_selection():
    word=0
    word = random.randint(0, len(words) - 1)
    return words[word]

# Below that, second function was written for putting slash , when the user saw.
def initialize(word):
    iniList = []
    for i in range(0,len(word)):
        if word[i] == " ":
            iniList.append(" ")
        else:
            iniList.append("-")

    return iniList

# Most important function is below that, first and second function is assigned
def taking_guess():

    word = random_selection()
    iniList = initialize(word)
    user_list = []
    remaining_guess = 6

    while remaining_guess > 0:
        # Below that i used to join. with print because, user should see without list but on the background, program
        # should process within list.
        print "Guess that belong to user:", ",".join(user_list)

        print "Guesses that are not used:", remaining_guess
        print "".join(iniList)

        letter = raw_input("Please, enter the letter to estimate\n").lower()
        user_list.append(letter)
        if letter not in word:
            remaining_guess = remaining_guess - 1 #if user enters wrong guess, remaining guess will decrease.
        elif letter == word:
            print user_name, "Congratulations! You have got it!" #if user finds whole all the word, program is done.
            remaining_guess = -1
        # Below that, if user finds word step by step, program is done.
        else:
            j = 0
            for i in word:
                if i == letter:
                    iniList[j] = i
                j += 1
            if list(word) == iniList:
                print "Word that you estimate " + word
                print user_name, "You won! Congratulations!"
                remaining_guess = -1
    if remaining_guess == 0:
        print user_name, "Your are failed but don't be upset, try again !"

#I wrote extra 2 function because of playing again or not.
#Below that I used to true-false for user's decision and identified in main function according to result.
def finish_of_continue():
    decision_for_playing_again = raw_input("Will you play again? YES or NO").lower()
    if decision_for_playing_again == "yes":
        return True
    elif decision_for_playing_again == "no":
        return False
    else:
        print "Wrong Input!"
        return finish_of_continue() #I wrote global in function because; if user want to play again, the program should repeat in itself.

# If user want to continue with decision that is taken from previous function, main function will execute.
def main():
    decision_for_playing_again = True
    while decision_for_playing_again:
        taking_guess()
        decision_for_playing_again = finish_of_continue()
main()
