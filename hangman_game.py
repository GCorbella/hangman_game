from random import choice

tries = 6
words = ["House","Potatoe","Boat","Gibberish","Witch","Cheese","Omelette","Bullfighter","Frederick","Taco","Sausage","Gypsy"]
letters_used =[]
correct_letters = []
incorrect_letters = []
guess = 0
endgame = False

def choose_word(palabras):
    chosen = choice(words).upper()
    chosen_unwords = len(set(chosen))

    return chosen, chosen_unwords

def ask_letter():
    letter = ""
    valid = False
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while not valid:
        letter = input("Please, enter a letter: ").upper()
        if (letter in abc) and (len(letter) == 1):
            if letter in letters_used:
                print("This letter have been selected before, choose another one")
            else:
                valid = True
                letters_used.append(letter)
    return letter

def show_new_screen(chosen):

    hidden_list = []

    for l in chosen:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append("-")

    print(" ".join(hidden_list))

def check_letter(letter,chosen,tries,coincidences):

    end = False

    if letter in chosen:
        correct_letters.append(letter)
        coincidences += 1
    else:
        incorrect_letters.append(letter)
        tries -= 1

    if tries == 0:
        end = loose()
    elif coincidences == chosen_unwords:
        end = win(chosen)

    return tries, end, coincidences

def loose():
    print("You loose. They hanged the man.")
    print("The word was " + chosen)

    return True

def win(chosen):
    show_new_screen(chosen)
    print("Congratulations, you found the hidden word!!!")

    return True



chosen, chosen_unwords = choose_word(words)

while not endgame:
    print("\n" + "*" * 20 + "\n")
    show_new_screen(chosen)
    print("\n")
    print("Used letters: " + " ".join(letters_used))
    print(f"Remaining tries: {tries}")
    print("\n" + "*" * 20 + "\n")
    letter = ask_letter()
    tries,endgame,guess = check_letter(letter,chosen,tries,guess)


