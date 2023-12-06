import random
import time

print("Hey! Time to play BOLLYWOOD/HOLLYWOOD!!")
time.sleep(0.5)
genre=input("HOLLYWOOD OR BOLLYWOOD?")
guesses=''
print("Start guessing...")
time.sleep(1)
if genre == "HOLLYWOOD":
    movies = ("tenet","orphan","inception","avatar","intersteller","avatar","joker","braveheart","seven","fukrey")
else:
    movies = ("queen","pathaan","chicchore","pk","heroine","fashion","devdas","zero","kick")

word = random.choice(movies)
turns = len(genre)
movie = word
t=list(genre)
while turns>0:
    wrong=0

    for char in word:
        if char in guesses.lower():
            print(char,end="")
        else:
                print("_",end="")
                wrong +=1
    if wrong == 0:
        print(" ")
        print("YOU WIN!!")
        print("The movie is: ",word)
        break
    print("\n")
    guess = input("guess a character:")
    guesses += guess
    if guess.lower() not in word:
        turns -= 1
        print("Wrong")
        t.pop()
        print("You have " + ("".join(t)) + " left")
        if turns==0:
            print("you lose")


