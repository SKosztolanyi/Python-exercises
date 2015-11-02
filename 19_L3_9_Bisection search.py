# This is a bisection search for user number
# The user has to indicate, whether his number is higher or lower than guessed
# I add an extra numG function to count number of guesses needed to guess the correct number.

print "Please think of a number between 0 and 100!"
numG=0
low = 0
high = 100
ans = (low+high)/2
while (ans <100):
    print "Is your secret number " +str(ans) + "?"
    guess = raw_input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess == "c":
        numG+=1
        break
    elif guess == "h":
        numG+=1
        high = ans
        ans = (low+high)/2
    elif guess == "l":
        numG+=1
        low = ans
        ans = (low+high)/2
    else:
        print "Sorry, I did not understand your input."
print "Game over. Your secret number was: "+ str(ans) +" Num of guesses: " + str(numG)