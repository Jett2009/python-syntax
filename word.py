def print_upper_words(words):
    """Print each word on separate line, uppercase."""

    for word in words:
        print(word.upper())


def print_upper_words_with_e(words):
    """Print each word on separate line, uppercase, if starts with e"""

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_word_given(words, must_start_with):
    """Print each word on separate line, uppercase, if starts with given letter """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


'''
In [33]: print_upper_word_given(['Brax','tony','break','ball','light'],{'b'})
BREAK
BALL
'''
