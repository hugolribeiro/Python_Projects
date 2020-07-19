import words_generator


# A function to hidden the word in _ _ _ _ _
def hide_a_word(chosen_word):
    hidden_word = [letter for letter in chosen_word]
    for letter in range(0, len(hidden_word)):
        hidden_word[letter] = '_'
    return hidden_word


# This function will create an alphabet, will print a greetings and will call the play function
def setup(chosen_word, hidden_word):
    shots = 0
    inputted_letters = []
    found = False
    chosen_word_list = list(chosen_word)
    print(
        f'Hello! Welcome to the Hangman game.\nYou will have 6 shots to try to got the word.'
    )
    print(f'\nThe secret word have {len(hidden_word)} letters')
    play(chosen_word, hidden_word, shots, chosen_word_list, found,
         inputted_letters)


# This function is the main function. Here contain the comparator
def play(chosen_word, hidden_word, shots, chosen_word_list, found,
         inputted_letters):
    while shots <= 6 and not found:
        print(hidden_word)
        if inputted_letters:
            print(f'Letters used at the moment: {inputted_letters}')
        letter = str(
            input('\nInput here a letter that you think have in this word: '))
        if len(letter) > 1:
            print(f'You only may input a single letter, please, try again')
            continue
        if not letter.isalpha():
            print(f'The letter must be inside the alphabet')
            continue
        if letter not in inputted_letters:
            inputted_letters.append(letter)
            inputted_letters.append(letter.upper())
            if (letter in chosen_word or letter.upper() in chosen_word.upper() or letter.upper(
            ) in chosen_word or letter in chosen_word.upper() or letter in chosen_word.lower()) and '_' in hidden_word:
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
        elif letter in inputted_letters:
            print(f'I am sorry, but this letter already was inputted')
            continue


word = words_generator.generate_word()
hide_word = hide_a_word(word)
setup(word, hide_word)
