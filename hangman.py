import random
import os


def generate_word():
    categorie = 0
    while categorie < 1 or categorie > 5:
        categorie = int(
            input(
                f'Please, choose the categorie and input the respective number: \n1 - Animal \n2 - Foods \n3 - Countries \n4 - Characters of fairy tale \n5 - I want to input a word\n'
            ))
    if categorie == 1:
        hidden_word(animal_list())
    elif categorie == 2:
        hidden_word(foods_list())
    elif categorie == 3:
        hidden_word(countries_list())
    elif categorie == 4:
        hidden_word(characters_list())
    elif categorie == 5:
        chosen_word = str(input('Input here the word: '))
        print('\n' * 70)
        hidden_word(chosen_word)


def animal_list():
    animals = [
        'cat', 'dog', 'fish', 'bird', 'crocodile', 'whale', 'shark', 'camel',
        'horse', 'ox', 'cow', 'scorpion', 'spider', 'frog', 'toad', 'duck',
        'eagle', 'lobster', 'ant', 'bee', 'fox', 'racoon', 'squirrel', 'tiger',
        'lion', 'wolf', 'snake'
    ]
    chosen_word = (animals[random.randint(0, len(animals) - 1)])
    return (chosen_word)


def foods_list():
    foods = [
        'apple', 'avocado', 'banana', 'cherry', 'grape', 'lemon',
        'watermeloon', 'melon', 'potato', 'onion', 'carrot', 'bread', 'pizza',
        'egg', 'hamburguer', 'meat', 'bacon', 'ham', 'sausage', 'fish',
        'salmon', 'lobster', 'corn', 'rice', 'bean', 'chocolate', 'sandwich',
        'soup'
    ]
    chosen_word = (foods[random.randint(0, len(foods) - 1)])
    return (chosen_word)


def countries_list():
    countries = [
        'Argentina', 'Brazil', 'Canada', 'Chile', 'China', 'Egypt', 'France',
        'Finland', 'Germany', 'Greece', 'Haiti', 'India', 'Italy', 'Jamaica',
        'Japan', 'Madagascar', 'Mexico', 'Morocco', 'Nigeria', 'Paraguay',
        'Peru', 'Portugal', 'Russia', 'Singapore', 'Sweden', 'Thailand',
        'Turkey', 'Uruguay', 'Venezuela', 'Vietnam'
    ]
    chosen_word = (countries[random.randint(0, len(countries) - 1)])
    return (chosen_word)


def characters_list():
    characters = [
        'mermaid', 'ogre', 'orc', 'goblin', 'angel', 'demon', 'knight',
        'warrior', 'archer', 'bard', 'magician', 'mage', 'wizard',
        'necromancer', 'monk', 'ghoul', 'dragon', 'unicorn', 'hunter',
        'merchant', 'thief', 'king', 'queen', 'princess', 'prince'
    ]
    chosen_word = (characters[random.randint(0, len(characters) - 1)])
    return (chosen_word)


#A function to hidden the word in _ _ _ _ _
def hidden_word(chosen_word):
    hidden_word = [letter for letter in chosen_word]
    for letter in range(0, len(hidden_word)):
        hidden_word[letter] = '_'
    setup(chosen_word, hidden_word)

#This function will create an alphabet, will print a greetings and will call the play function 
def setup(chosen_word, hidden_word):
    shots = 0
    inputed_letters = []
    found = False
    alphabet = 'abcçdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZÇ'
    chosen_word_list = list(chosen_word)
    os.system('clear') or None
    print(
        f'Hello! Welcome to the Hangman game.\nYou will have 6 shots to try to got the word.'
    )
    print(f'\nThe secret word have {len(hidden_word)} letters')
    play(chosen_word, hidden_word, shots, chosen_word_list, alphabet, found,
         inputed_letters)


#This function is the main function. Here contain the comparator 
def play(chosen_word, hidden_word, shots, chosen_word_list, alphabet, found,
         inputed_letters):
    while shots <= 6 and found == False:
        print(hidden_word)
        letter = str(
            input('\nInput here a letter that you think have in this word: '))
        if len(letter) > 1:
            print(f'You only may input a single letter, please, try again')
            continue
        if letter not in inputed_letters:
            inputed_letters.append(letter)
            inputed_letters.append(letter.upper())
        elif letter in inputed_letters:
            print(f'I am sorry, but this letter already was inputted')
            continue
        if letter not in alphabet:
            print(f'The letter must be inside the alphabet')
        else:
            if (letter in chosen_word or letter.upper() in chosen_word.upper(
            ) or letter.upper() in chosen_word or letter in chosen_word.upper() or letter in chosen_word.lower()) and '_' in hidden_word:
                for char in range(len(chosen_word)):
                    if chosen_word[char] == letter:
                        hidden_word[char] = letter
                    elif chosen_word[char] == letter.upper():
                        hidden_word[char] = letter.upper()
                    elif chosen_word[char] == letter.lower():
                        hidden_word[char] = letter.lower()
                if chosen_word_list == hidden_word:
                    print(
                        f'\nCongrats, you win! \nThe word was: {chosen_word}')
                    return
            elif letter not in chosen_word or letter not in chosen_word.upper():
                shots += 1
                print(
                    f'This letter is incorrect! Actual number of shots: {shots}'
                )
                if shots > 5:
                    print(
                        f'Ow, no! {shots} shots. You failed! :( \nThe word was: {chosen_word}'
                    )
                    return


generate_word()
