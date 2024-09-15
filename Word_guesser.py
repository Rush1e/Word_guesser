


import random

word_bank=['avatar','avengers','titanic','barbie','oppenheimer','deadpool']

word= random.choice(word_bank)

guessedword=[' _ ']*len(word)

lives=10

while lives > 0 :
    print("\n Current word: " + ''.join(guessedword))
    guess= input("Write a letter").lower()
    if guess in word:
        for i in range(len(word)):
                if word[i] == guess:
                    guessedword[i] = guess
                   
    else:
        lives = lives-1
        print(f"Uhoh, you have {lives} lives left" )
    if ' _ ' not in guessedword:
        print(f"\n Congrats You win!! \n the movie was {word}" )
        break
else:
    print(f"\n You lost , the movie was {word}")
    








