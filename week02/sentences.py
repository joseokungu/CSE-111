####################
# Date: 2024-09-29
# File: sentences.py
# Author: Jose Okitandende
# Class: CSE 111
# Purpose: 02 Prove Milestone: Outdoor Scene
#####################

import random

"""
Write and test functions that generate sentences with three parts:
    1. a determiner (sometimes known as an article)
    2. a noun
    3. a verb
    4. a prepositional phrase

For example:
    One girl talked for the car.
    A bird drinks off one child.
    The child will run on the car.
    Some dogs drank above many rabbits.
    Some children laugh at many dogs.
    Some rabbits will talk about some cats.

Write the main function and any other functions 
that you think are necessary for your program to 
generate and print six sentences with these characteristics:

Quantity	Verb Tense
a.	single	past
b.	single	present
c.	single	future
d.	plural	past
e.	plural	present
f.	plural	future
"""

def main():
    """
    This program generates simple English sentences.
    This program has three different methods to generate those simple English sentences.
      
    (1) It can call the function random_sentence_generator to specify any specified parameters as the number of sentences.
    (2) It can call the function get_sentence_by_list, this will generate the specified number of sentences as required in the assignment.
    (3) It can call the function get_sentence, an it will generate one sentence at a time with the specified parameters.
    """

    """Call the get_random_sentence_generator function
    generate a random number of sentences with specified parameter"""
    random_sentence_generator(20)

    """Call the get_sentence_by_list function
    generate sentences with the parameters specified in the list"""
    # get_sentence_by_list()

    """Call the get_sentence function
    generate one sentence with parameters specified"""
    # get_sentence(0, "past")

def make_sentence(quantity, tense):
    '''Returns a randomly generated word by calling
    get_determiner, get_noun, get_verb.
    Parameter
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: prints a randomly generated sentence.
    '''
    d = get_determiner(quantity).capitalize()
    n = get_noun(quantity)
    v = get_verb(quantity, tense)
    p = get_prepositional_phrase(quantity)
    a = get_adverb()

    sentence =(f"{d.capitalize()} {n} {a} {v} {p}.")
    print(sentence)

def make_sentence_by_list():
    '''Returns a randomly generated word by calling
    get_determiner, get_noun, get_verb.
    Parameter
        None - update list to determine sentence structure and length.
    Return: prints a number of randomly generated sentences.
    '''
    list = [(1, "past"), (1, "present"), (1, "future"), (0, "past"), (0, "present"), (0, "future")]
    
    for quantity, tense in list:
        d = get_determiner(quantity).capitalize()
        n = get_noun(quantity)
        v = get_verb(quantity, tense)
        p = get_prepositional_phrase(quantity)
        a = get_adverb()

        sentence =(f"{d.capitalize()} {n} {a} {v} {p}.")
        print(sentence)

def random_sentence_generator(number=7):
    '''Returns a randomly generated word by calling
    get_determiner, get_noun, get_verb.
    Parameter
        number: an integer.
            The default is 7
    Return: prints a number of randomly generated sentences.
    '''
    quantity = random.choice([0,1])
    tense = random.choice(["past", "present", "future"])

    for _ in range(number):
        d = get_determiner(quantity).capitalize()
        n = get_noun(quantity)
        v = get_verb(quantity, tense)
        p = get_prepositional_phrase(quantity)
        a = get_adverb()

        sentence =(f"{d.capitalize()} {n} {a} {v} {p}.")
        print(sentence)

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if (quantity != 1 or quantity == 1) and tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1 and tense == "present":
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif (quantity != 1 or quantity == 1) and tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", 
        "out", "over", "past", "to", "under", "with", "without"]
    # Randomly choose and return a determiner.
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or plural.
    Return: a prepositional phrase.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()
    adjective = get_adjective()

    prepositional_phrase = (f"{preposition} {determiner} {adjective} {noun}")

    return prepositional_phrase
    
def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "good", "new", "first", "last", "long", 
        "great", "little", "own", "other", "old", 
        "right", "big", "high", "different", "small", 
        "large", "next", "early", "young", "important", 
        "few", "public", "bad", "same", "able"

    Return: a randomly chosen adjective.
    """
    adjectives = ["good", "new", "first", "last", "long", "great", "little", "own", "other", "old", "right", "big", "high", 
    "different", "small", "large", "next", "early", "young", "important", "few", "public", "bad", "same", "able"]

    # Randomly choose and return a adjective.
    adjective = random.choice(adjectives)
    return adjective

def get_adverb():
    """An adverb is a word or an expression that generally modifies a verb,
    adjective, another adverb, determiner, clause, preposition, or sentence. 
    
    Return a randomly chosen adverb
    from this list of adverbs:
        "slowly", "fast", "carefully", "carelessly", "effortlessly", 
        "urgently", "always", "almost always", "usually", 
        "often", "sometimes", "occasionally", "seldom", "rarely", 
        "almost never","never", "quietly", "possibly", "incredibly", 
        "probably", "luckily", "happily", "angrily", "ironically", "basically"

    Return: a randomly chosen adverb.
    """
    adverbs =  ["slowly", "fast", "carefully", "carelessly", "effortlessly", "urgently", "always", "almost always", "usually", 
    "often", "sometimes", "occasionally", "seldom", "rarely", "almost never","never", "quietly", "possibly", "incredibly", "probably",
    "luckily", "happily", "angrily", "ironically", "basically"]
   

    # Randomly choose and return a adjective.
    adverb = random.choice(adverbs )
    return adverb

# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()