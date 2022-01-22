# importing all required modules
import random as r
import string

# setting up nessesary variables and lists
alphabets = list(string.ascii_letters)
digits = list(string.digits)
med_spe_characters = list("!@#$%^&*()")
high_spe_characters = list("!@#$%^&*()_-+={[}]|\:;\"\'<,>.?/~`")


"""This is a function that randomizes the upper
and lowercases in your key phrase in high security"""


def randomcase(s):
    result = ''
    for c in s:
        if c in alphabets:
            case = r.randint(0, 1)
            if case == 0:
                result += c.upper()
            else:
                result += c.lower()
        else:
            result += c
    return result


"""This class holds the generation codes for all base pw security
levels"""


class GenPro:
    def __init__(self, p_length, must_phrase, type_count, password):
        self.p_length = p_length
        self.must_phrase = must_phrase
        self.type_count = type_count
        self.password = password

    def low_secur(self):  # low security
        for i in range(int(self.p_length) - len(self.must_phrase)):
            typpe = r.choice(self.type_count)
            if typpe == "num":
                self.password.append(r.choice(digits))
            else:
                self.password.append(r.choice(alphabets))

        for i in range(1, int(self.p_length) - len(self.must_phrase)):
            self.password[i] = self.password[i].lower()

    def med_secur(self):  # medium security
        for i in range(self.p_length - len(self.must_phrase)):
            typpe = r.choice(self.type_count)
            if typpe == "num":
                self.password.append(r.choice(digits))
            elif typpe == "let":
                self.password.append(r.choice(alphabets))
            else:
                self.password.append(r.choice(med_spe_characters))

    def high_secur(self):  # high security
        self.must_phrase = randomcase(self.must_phrase)
        self.password.clear()
        self.password.append(self.must_phrase)

        for i in range(self.p_length - len(self.must_phrase)):
            typpe = r.choice(self.type_count)
            if typpe == "num":
                self.password.append(r.choice(digits))
            elif typpe == "let":
                self.password.append(r.choice(alphabets))
            elif typpe == "sym":
                self.password.append(r.choice(high_spe_characters))

    def common_website_requirements(self):  # recommended security
        x = 0
        for i in range((self.p_length - 4) - len(self.password[0])):
            x = r.randrange(1, 3)
            if x != 2:
                self.password.append(r.choice(digits))
            else:
                self.password.append(r.choice(alphabets))

        # recommended security can satisfy 90% of website
        # registeration by having at least one upper and
        # lower case letters, one number and one symbol
        self.password.append(r.choice(alphabets).lower())
        self.password.append(r.choice(digits))
        self.password.append(r.choice(alphabets).upper())
        self.password.append(r.choice(med_spe_characters))
