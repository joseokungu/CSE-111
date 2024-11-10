"""
Program: chemistry
Author: Jose Okitandende
Purpose: Writing functions to calculate molar mass of substances
Date: 31/10/2024
"""


from password_manager import password_gen
from random import choice, randint, shuffle
import pytest


def test_password_gen():
    characters = ["A", "b", "C", "d", "E", "f", "G", "h", "I", "j", "K", "l", "M", "n", "O", "p", "Q", "r", "S",
                  "t", "U", "v", "W", "x", "Y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "!!", "~", "@", "#", "`", "//",
                  "|", ">", "**", "+", "&", "^", "%", "$", ":", ";", "?", "<<", "(", ")", "{", "]", "''", "_", "--"]
    password_list = [choice(characters) for _ in range(randint(8, 10))]
    shuffle(password_list)
    the_password = "".join(map(str, password_list))
    word = password_gen()
    assert word == word
    password = the_password.split()
    for _ in range(5):
        assert password[0] in password
        assert password[1] in password
        assert password[2] in password
        assert password[3] in password
        assert password[4] in password
        assert password[5] in password
        assert password[6] in password
        assert password[7] in password
        assert password[8] in password
        assert password[9] in password


pytest.main()