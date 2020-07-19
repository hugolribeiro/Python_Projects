import random

def generate_word():
    categorie = 0
    while categorie < 1 or categorie > 5:
        categorie = int(
            input(
                f'Please, choose the categorie and input the respective number: \n1 - Animal \n2 - Foods \n3 - '
                f'Countries \n4 - Characters of fairy tale \n5 - I want to input a word\n '
            ))
    if categorie == 1:
        term = animal_list()
    elif categorie == 2:
        term = foods_list()
    elif categorie == 3:
        term = countries_list()
    elif categorie == 4:
        term = characters_list()
    elif categorie == 5:
        term = str(input('Input here the word: '))
        print('\n' * 70)
    return term


def animal_list():
    animals = [
        'cat', 'dog', 'fish', 'bird', 'crocodile', 'whale', 'shark', 'camel',
        'horse', 'ox', 'cow', 'scorpion', 'spider', 'frog', 'toad', 'duck',
        'eagle', 'lobster', 'ant', 'bee', 'fox', 'racoon', 'squirrel', 'tiger',
        'lion', 'wolf', 'snake'
    ]
    chosen_word = (animals[random.randint(0, len(animals) - 1)])
    return chosen_word


def foods_list():
    foods = [
        'apple', 'avocado', 'banana', 'cherry', 'grape', 'lemon',
        'watermelon', 'melon', 'potato', 'onion', 'carrot', 'bread', 'pizza',
        'egg', 'hamburguer', 'meat', 'bacon', 'ham', 'sausage', 'fish',
        'salmon', 'lobster', 'corn', 'rice', 'bean', 'chocolate', 'sandwich',
        'soup'
    ]
    chosen_word = (foods[random.randint(0, len(foods) - 1)])
    return chosen_word


def countries_list():
    countries = [
        'Argentina', 'Brazil', 'Canada', 'Chile', 'China', 'Egypt', 'France',
        'Finland', 'Germany', 'Greece', 'Haiti', 'India', 'Italy', 'Jamaica',
        'Japan', 'Madagascar', 'Mexico', 'Morocco', 'Nigeria', 'Paraguay',
        'Peru', 'Portugal', 'Russia', 'Singapore', 'Sweden', 'Thailand',
        'Turkey', 'Uruguay', 'Venezuela', 'Vietnam'
    ]
    chosen_word = (countries[random.randint(0, len(countries) - 1)])
    return chosen_word


def characters_list():
    characters = [
        'mermaid', 'ogre', 'orc', 'goblin', 'angel', 'demon', 'knight',
        'warrior', 'archer', 'bard', 'magician', 'mage', 'wizard',
        'necromancer', 'monk', 'ghoul', 'dragon', 'unicorn', 'hunter',
        'merchant', 'thief', 'king', 'queen', 'princess', 'prince'
    ]
    chosen_word = (characters[random.randint(0, len(characters) - 1)])
    return chosen_word