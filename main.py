multiple_strings = ['noon', 'night', 'day', 'bulb']


def same_character_words(matched_letters):
    counter = 0
    word = 0
    while word < len(matched_letters): 
        if (matched_letters[word][0]) ==                (matched_letters[word][-1]):
          counter += 1
        word += 1
    return counter

print(same_character_words(multiple_strings))