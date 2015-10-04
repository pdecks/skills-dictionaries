# Tricia Decker

# To work on the advanced problems, set to True
ADVANCED = True

import string  # for alternate solution to encode()


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    unique_words = {}
    words = input_string.strip().split()
    for word in words:
        if word in unique_words.keys():
            unique_words[word] += 1
        else:
            unique_words[word] = 1

    return unique_words


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]


    """
    #########################################################################
    ## Hey Cynthia, let's talk about this on Tuesday
    ## I found this one really tricky without being able to use 'if __ in __'
    ## also, the rules are a bit unclear for duplicates in BOTH lists
    ## >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 1, 2, 3, 4]))
    ##        [1, 1, 2, 2] ?
    ## or ... [1, 1, 1, 2, 2, 2] ?
    ## or ... [1, 1, 1, 1, 2, 2, 2, 2] ?
    #########################################################################

    # merge the lists in a new list (do not mutate original lists!)
    # create a copy of list 1
    union_list = list1[::]
    # extend list 2 onto copy of list 1
    union_list.extend(list2)

    # create a dictionary of the union of the lists
    # keys = unique integers, values = number of times int appears in union
    union = dict([val, union_list.count(val)] for val in union_list)

    # add values that appeared in both lists to a new list
    shared_list = []
    for key in union:
        # return keys with value > 1 (appears in both list)
        if union[key] > 1:
            # return the key multiple times
            for i in range(union[key]-1):
                shared_list.append(key)

    return shared_list

    # other ideas ...
    # evaluate set(list1) and set(list2) to determine which has larger number
    # of unique values.
    # unique = set(list1).intersection(list2)


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    # Same approach as find_common_items, only the nested for loop
    # is eliminated such that shared items only print once

    union_list = list1[::]
    # extend list 2 onto copy of list 1
    union_list.extend(list2)

    # create a dictionary of the union of the lists
    # keys = unique integers, values = number of times int appears in union
    union = dict([val, union_list.count(val)] for val in union_list)

    # add values that appeared in both lists to a new list
    shared_list = []
    for key in union:
        # return keys with value > 1 (appears in both list)
        if union[key] > 1:
            shared_list.append(key)

    return shared_list


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # similar approach as for find_unique_common_items
    # initially updated if statement in dict-to-list conversion
    # before realizing that i was just returning dict.keys()
    word_counts = dict([word, words.count(word)] for word in words)

    # add values that appeared in both lists to a new list
    unique_list = word_counts.keys()

    return unique_list


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    encode_dict = {'e': 'p', 'a': 'd', 't': 'o', 'i': 'u'}

    encoded = ''

    for char in phrase:
        if char in encode_dict.keys():
            # replace with substitute character
            encoded += encode_dict[char]
        else:
            encoded += char

    # ALTERNATE non-dictionary solution, comment out lines 181-190
    # note: had to import string at beginning of file
    # encoded = phrase
    # encoded = phrase.translate(string.maketrans("eati", "pdou"))

    return encoded


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    # create a dictionary where key = word length and value = list of words
    length_dict = {}
    for word in words:
        if len(word) in length_dict.keys():
            length_dict[len(word)].append(word)
        else:
            length_dict[len(word)] = [word]

    # convert the dictionary to tuples
    return length_dict.items()


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    #########################################################################
    # Hey Cynthia, is there a better way to handle the punctuation?
    # ... nevermind. I built it to handle the punctuation and then realized
    # that we are to ignore punctuated words (not translate them)
    #########################################################################

    # create list of english words to be translated
    eng = ['sir', 'hotel', 'student', 'boy', 'madam', 'professor',
           'restaurant', 'your', 'excuse', 'students', 'are', 'lawyer', 'the',
           'restroom', 'my', 'hello', 'is', 'man']

    # create pirate-speak equivalent list
    pir = ['matey', 'fleabag inn', 'swabbie', 'matey', 'proud beauty',
           'foul blaggart', 'galley', 'yer', 'arr', 'swabbies', 'be',
           'foul blaggart', "th'", 'head', 'me', 'avast', 'be', 'matey']

    # merge lists into an English-to-Pirate dictionary
    eng_to_pir = dict([eng[i], pir[i]] for i in range(len(eng)))

    # break phrase into words
    words = phrase.split(" ")

    # translate the phrase
    translated = []
    for word in words:
        # if punctuation present, strip it off word
        punc = ''
        ## is 298-305 is uncommented, punctuation can be handled ############
        # while not word[len(word)-1].isalpha():
        #     # print "This is the last character: {}".format(word[len(word)-1])
        #     # save punctuation to add at end
        #     punc += word[len(word)-1]
        #     # update word
        #     word = word[:len(word)-1]
        # # reverse the punctuation string
        # punc = punc[::-1]

        # if word is in dictionary, translate it
        if word in eng_to_pir.keys():
            current_word = eng_to_pir[word]+punc
        else:
            current_word = word+punc
        translated.append(current_word)

        translated_phrase = " ".join(translated)

    return translated_phrase

# # End of skills. See below for advanced problems.
# # To work on them, set ADVANCED=True at the top of this file.
# ############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the
    most in the input string.

    If there is a tie, the order of the letters in the returned list should be
    alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
    ##########################################################################
    # Hey Cynthia, is there a more efficient way to compile my max_list
    # without losing the speed of my dictionary?
    ##########################################################################

    # create a dictionary where key = character, value = # of times char appears
    letter_count = dict([char, input_string.count(char)] for char in input_string if char.isalpha())

    # find the max # of appearances of any char
    max_val = max(letter_count.values())

    # create list of char(s) that match that max # of appearances
    max_list = []
    for key in letter_count:
        if letter_count[key] == max_val:
            max_list.append(key)

    return max_list


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    ##########################################################################
    # Hey Cynthia, I'd like to talk about the "one call" solution. I was
    # reading on the optional key argument for sorted() but couldn't figure it out
    ##########################################################################

    # THIS IS sort_by_word_length(words)
    # create a dictionary where key = word length and value = list of words
    length_dict = {}
    for word in words:
        if len(word) in length_dict.keys():
            length_dict[len(word)].append(word)
        else:
            length_dict[len(word)] = [word]

    # sort the nested list of words (the values in the dictionary)
    for key in length_dict:
        length_dict[key].sort()
    # convert the dictionary to tuples
    return length_dict.items()


    # sort the tuple lists with one call
    # sorted(word_tup, key=lambda tup: tup[1])
    # return


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
