# Python CS final project - Password Generator
# Michael Zhu
# Jan 20th, 2022
# CS30
# Ms.S

"""This is a program that allows you to generate passwords with
great amounts of flexibility. You have by default four security
levels to choose from, with each one being a little different
from one another. If you are not satisfied you can use the
advanced generator after using the normal one once to
customize your password even greater. After you are done
you can either generate more, quit or save the pws to your
computer"""
# Importing all the modules needed
import string
import random as r
import time
import PwGenProcess as PGen
import AdvancedPwSett as APS
import PwSave

# Setting up the different variables that are going to be used
# within the code
alphabets = list(string.ascii_letters)  # letters word bank

type_count = ["num", "let", "sym"]  # A few lists storing important info
password = []  # the list that is going to hold the password
final_pw_list = []  # the list that holds every pw generated

checkp_1 = 1  # Checkpoints
checkp_2 = 1

# the while loop that ensures the code runs forever till told to stop
while True:
    print("welcome to password generator. This is a place for you to " +
          "develop a satisfactory password with great levels of " +
          "customization. \ntype anything to start, and type quit to " +
          "stop the program\n")
    touch = input()
    if touch == "quit":  # stop
        break

    time.sleep(1)

    # asks for length of password and deals with inproper inputs
    try:
        p_length = int(input("what is the length of your desired password?\n"))
        if p_length < 4:
            print("an accepted password must be at least 4 characters long\n")
            continue
    except ValueError:
        print("please input a number\n")
        continue
        time.sleep(1)

    time.sleep(1)

    # checkpoint 1, keeps looping until an acceptable answer is inputted
    while checkp_1 == 1:
        # asks for the key phrase in password
        must_phrase = input("type in a phrase that you would like to have " +
                            "included in the password, if this doesn't " +
                            "apply to you, press the enter key. Please " +
                            "make sure this phrase is not included in " +
                            "your username for maximium sercurity\n")

        if must_phrase == "\n":
            must_phrase = ""
            checkp_1 -= 1
        elif len(must_phrase) > p_length - 4:
            print("the phrase is too big for the allowed length of " +
                  "password, try again\n")
            continue
        else:
            checkp_1 -= 1

    checkp_1 = 1

    # checkpoint 2, works the same as the previous
    while checkp_2 == 1:
        security_lvl = str(input("What is the level of security you are " +
                                 "looking for?\n\t- low: relatively easier " +
                                 "to memorize, with enough length " +
                                 "also difficult to guess\n\t" +
                                 "- medium: need to write it down, includes " +
                                 "different characters and more randomized" +
                                 "\n\t- high: for the most secure files and " +
                                 "accounts, your must included phrase might" +
                                 "\n\t  be manipulated slightly, " +
                                 "impossible to remember, impossible to " +
                                 "guess\n\t- recommended: a password that " +
                                 "satisfies most websites and account " +
                                 "registeration\n\t  platforms for your " +
                                 "convenience\n"))  # asks for security lvls

        # if improper input happens
        if security_lvl.lower() != "low" and security_lvl.lower() != "med" \
           and security_lvl.lower() != "medium" and security_lvl.lower() != \
           "high" and "recom" not in security_lvl.lower():
            if security_lvl == "quit":
                break
            else:
                print("value not accepted!")
                continue
        else:
            checkp_2 -= 1

    if security_lvl == "quit":  # quits if the improper input is "quit"
        break

    time.sleep(0.5)
    print("generating...")
    time.sleep(1)

    # puts in the key phrase
    password.append(must_phrase)

    # actual generation for password depending on the security level
    # this will run 3 times to generate 3 possible passwords
    for i in range(3):
        result = PGen.GenPro(p_length, must_phrase, type_count, password)

        if security_lvl.lower() == "low":  # low security
            result.low_secur()

        elif security_lvl.lower() == "med" or security_lvl.lower() == "medium":
            result.med_secur()  # medium security

        elif security_lvl.lower() == "high":  # high security
            result.high_secur()

        elif "recom" in security_lvl.lower():  # recommended security
            result.common_website_requirements()

        r.shuffle(result.password)
        print("".join(result.password) + " could be your password")
        time.sleep(0.7)

        # prints out and resets the password list
        final_pw_list.append("".join(result.password))
        password.clear()
        password.append(must_phrase)

    time.sleep(1)

    checkp_2 = 1

    # the end of program but allows other things to be done
    # see line in cont_ask to find out what else could be done
    while True:
        cont_ask = input("do you want to generate more password? type quit " +
                         "to stop the program, continue to use again, " +
                         "advanced to access the advanced generator, or save" +
                         " to save the generated passwords\n")  # things to do

        if "quit" in cont_ask.lower():  # quit
            break
        elif "cont" in cont_ask.lower():  # use again
            break
        elif "adv" in cont_ask.lower():  # use the advanced generator
            time.sleep(1)
            password.clear()
            APS.pw_manipulation(password, final_pw_list)
        elif "sav" in cont_ask.lower():  # save the passwprd
            PwSave.file_save(final_pw_list)
        else:
            print("invalid input!")  # handles wrong inputs

    # breaks or restarts the overall loop
    if "quit" in cont_ask.lower():
        break
    elif "cont" in cont_ask.lower():
        continue
