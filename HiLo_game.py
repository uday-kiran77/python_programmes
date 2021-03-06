#Python program to play hilo game
#User should think of a number between mentioned range and tell the computer that the number guessed by computer is high  or low from your guess
#Computer can find the number of you think in maximum of 10 guesses
#This program uses Binary search algorithm

low=1
high=1000
print("Please think of a number between {} and {}".format(low,high))
input("press ENTER to start")
guesses=0

while low != high:
    guess=low+(high-low)//2

    high_low=input("\nMy guess is {}.\nShould i guess higher or lower? Enter h (High), l (Low) or c (Correct) if my guess is correct ".format(guess)).casefold()

    if high_low=='h':
        low=guess+1
        guesses+=1
    elif high_low == 'l':
        high=guess-1
        guesses+=1
    elif high_low == 'c':
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please Enter h,l or c")
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
