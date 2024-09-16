"""Convert a word to pig latin"""

import string
import textwrap
import pyperclip


def main():
    """Take a word from the user and convert it to pig latin."""

    print("\n\n")
    print("Welcome to the Pig Latin converter.")

    while True:
        user_input = input("Please enter a word or phrase.\n\n")

        # Split the string into a list
        input_list = user_input.split()

        result_text = ' '.join([get_pig_latin_word(w) for w in input_list])
        print(textwrap.fill(result_text))

        pyperclip.copy(result_text)
        print("\n\n****************************************************************************")
        print("Result copied to clipboard.")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break


def starts_with_vowel(word):
    """Get the first letter of a word and check if it is a vowel."""

    is_vowel = False
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower() in vowels:
        is_vowel = True
    return is_vowel


def get_pig_latin_word(word):
    """Format given word in pig latin, taking punctuation into account"""

    last_char_in_word = word[-1]
    word_ends_with_punctuation = False
    first_char_upper = False
    if last_char_in_word in string.punctuation:
        word_ends_with_punctuation = True

    if word[0].isupper():
        first_char_upper = True

    pig_latin_word = ""

    if word_ends_with_punctuation:
        # If the word starts with a vowel and has punctuation, add 'way'
        # and the punctuation to the end of the word.
        if starts_with_vowel(word):
            pig_latin_word = word[:-1].lower() + f"way{last_char_in_word}"
        else:
            # Else add the first letter to the end and append 'ay' if it is a consonant
            pig_latin_word = word[1:-1].lower() + word[0].lower() + f"ay{last_char_in_word}"

    else:
        if starts_with_vowel(word):
            pig_latin_word = word.lower() + f"way"
        else:
            # Else add the first letter to the end and append 'ay' if it is a consonant
            pig_latin_word = word[1:].lower() + word[0].lower() + f"ay"

    if first_char_upper:
        pig_latin_word = list(pig_latin_word)
        pig_latin_word[0] = pig_latin_word[0].upper()
        pig_latin_word = "".join(pig_latin_word)

    return pig_latin_word


if __name__ == "__main__":
    main()
