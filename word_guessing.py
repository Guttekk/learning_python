import random 

def get_random_word():
    words = ["cytryna", "banan","arbuz", "limonka", "malina"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print(character, end=" ")
    print("")

def get_guess():
    print("Enter a letter: ")
    return input()

def process_letter(letter, word, blanked_word):

    result = False

    for i in range(0, len(word)):
        if word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result

def print_strikes(strikes):
    for i in range(0, strikes):
        print("X", end="")
    print("")

def play_word_game():

    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()
    blanked_word = list("_" * len(word))

    while playing:

        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False


    if strikes >= max_strikes:
        print("You lose!")
    else:
        print("Winner!")
   

print("Games started!")

play_word_game()
