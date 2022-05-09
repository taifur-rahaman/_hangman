import random
import hangman_img

word_list = ["preamble", "presage", "prescient", "predilection", "predicate", "predicate", "presentiment", "presentiment"]

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

random_word = random.choice(word_list)

placeholder = []
for _ in range(len(random_word)):
    placeholder.append("_")

print(f"\nPsst the answer is {random_word}")

end_game = False
lives = 6

while True:
    if "_" in placeholder:
        user_guess = input("Guess a letter: ").lower()
        i = 0
        if user_guess not in random_word:
            lives -= 1
            print(f"Lives remaining: {lives}")
            print(hangman_img.hangman_img[6-lives])

        if lives > 0:
            for _ in range(len(random_word)):
                if random_word[i] == user_guess:
                    placeholder[i] = user_guess
                i+= 1
            print(placeholder)
        else:
            print("Game Over")
            exit()
    else:
        print("You Won")
        break
