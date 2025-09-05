def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    char_dict = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter not in char_dict:
            char_dict[lower_letter] = 1
        else:
            char_dict[lower_letter] += 1

    return char_dict

def sorted_characters(dict):
    characters = []
    for char in dict:
        if char.isalpha():
            characters.append({
                "char": char,
                "num": dict[char],
            })

    characters.sort(reverse=True, key=sort_on)
    return characters


def sort_on(items):
    return items["num"]