"""Convert a word to pig latin"""

import string
import textwrap


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

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


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

    # If the word starts with a vowel but has punctuation, add 'way'
    # and the punctuation to the end of the word.
    #
    # Else if the word starts with a vowel but doesn't have punctuation,
    # simply add 'way' to the end of it.
    #
    # If the last character in a word is punctuation and the word starts with a
    # consonant, add the punctuation after adding the Pig latin to the
    # end of the word (e.g. 'along,' becomes 'longaway,') with the comma
    # at the end as expected.
    #
    # Else move the first letter of the word to the end and
    # add 'ay' to the end.
    if word[0].isupper():
        first_char_upper = True
    word_result = word[:-1].lower() + f"way{last_char_in_word}" \
        if word_ends_with_punctuation \
        else word.lower() + "way" if starts_with_vowel(word) \
        else word[1:-1].lower() + word[0].lower() + f"ay{last_char_in_word}" \
        if word_ends_with_punctuation \
        else word[1:].lower() + word[0].lower() + "ay"

    if first_char_upper:
        word_result = list(word_result)
        word_result[0] = word_result[0].upper()
        word_result = "".join(word_result)

    return word_result


if __name__ == "__main__":
    main()
