# Importing the modules
import random as r
import string
import time

# Added the character banks the password could choose from
alphabets = list(string.ascii_letters)  # all the letters
digits = list(string.digits)  # all the numbers
med_spe_characters = list("!@#$%^&*")  # some of the symbols
# all the symbols
high_spe_characters = list("!@#$%^&*()_-+={[}]|\:;\"\'<,>.?/~`")

# Menu for advanced generator
menu = ["select desired character types", "set amount of desired characters",
        "provide word of interest", "prohibit characters",
        "generate password", "quit"]


"""This is the funcion to detect types of characters in passwords"""


def type_detection(charr):
    if charr in alphabets:
        typpe = alphabets
    elif charr in digits:
        typpe = digits
    else:
        typpe = high_spe_characters
    return typpe  # the type of characters


"""The function that executes the advanced generator"""


def pw_manipulation(password, save):

    # Creates variables for detailed questions later on
    checkp_1 = 1
    num_leng_ask = 0
    let_leng_ask = 0
    case_ask = "a"
    sym_leng_ask = 0

    # Greetings
    print("welcome to the advanced settings menu, you can customize your" +
          " password with even\ngreater flexibility in here\n")

    time.sleep(2)

    aska = input("what is your key phrase? if none press enter. " +
                 "Please ensure this phrase does not\nexist in your " +
                 "username\n")  # gets the key phrase

    # If none were inputted key phrase doens't exist
    if aska == "\n":
        aska = ""
    password.append(aska)

    time.sleep(1.5)
    print("Please note that the first two options that will be displayed " +
          "are manetory")
    time.sleep(1.5)

    # The loop that controls the menu
    while True:
        print("You can:\n")
        count = 1  # number before menu option
        for i in menu:  # The previously mentioned menu
            print(str(count) + ". " + i)
            count += 1
            print("\t")

        time.sleep(2)

        # accepts input to choose options from menu
        menu_ask = input("Type 1 for the 1st option, 2 for the 2nd option, " +
                         "and so on, type quit to end the program\n")

        # Select types of characters
        if menu_ask == "1":
            print("you can have:\n\t- numbers\n\t- letters\n\t- symbols\n")
            type_ask = input("which type(s) of characters do you want in " +
                             "your password? type all that apply before " +
                             "pressing enter\n")
            time.sleep(0.5)
            print("Preference(s) noted\n")

        # Enter amount of selected characters
        elif menu_ask == "2":
            # If number in selection
            if "number" in type_ask.lower():
                # get the length of numbers
                num_leng_ask = int(input("how many numbers do you want in " +
                                         "your password?\n"))
                time.sleep(0.5)
                print("understood")

            # If letter in selection
            if "letter" in type_ask.lower():
                # get the length of letters
                let_leng_ask = int(input("how many letters do you want in " +
                                         "your password?\n"))
                time.sleep(0.5)

                # A checkpoint to accept bad inputs and loop it again till
                # Correct input could happen
                while checkp_1 > 0:
                    # Selecting upper, lowercase or both in letter
                    if let_leng_ask < 2:
                        case_ask = input("do you desire upper or lowercase?\n")
                        if "upp" not in case_ask and "low" not in case_ask:
                            print("there's only one character cannot be both")
                            continue
                    else:
                        case_ask = input("do you desire upper, lowercase " +
                                         "or both?")
                    if case_ask.lower() != "both" and "upper" not in \
                       case_ask.lower() and "lower" not in case_ask.lower():
                        print("unaccepted value!")
                    else:
                        print("noted")
                        checkp_1 -= 1

                time.sleep(0.5)

            # If symbol in selection
            if "symbol" in type_ask.lower():
                # get the length of symbols
                sym_leng_ask = int(input("how many symbols do you want in " +
                                         "your password?\n"))
                time.sleep(0.5)
                print("ok")

            # Failsafe
            if "number" not in type_ask.lower() and "letter" not in \
               type_ask.lower() and "symbol" not in type_ask.lower():
                print("You haven't selected your character types yet, " +
                      "please go back and do so\n")

        # Accepts words of interest
        elif menu_ask == "3":
            print("what are your word(s) of interest? This will assist you " +
                  "in better memorization of the\npassword. Separate by " +
                  "space and press enter when finished\n")
            int_phrase_ask = input("")
            int_phrase_ask = int_phrase_ask.split(" ")

        # Prohibits characters
        elif menu_ask == "4":
            print("Type in all the characters you do not want to have in " +
                  "the final product, press enter after you are finished. " +
                  "Note that this will NOT affect your inputted phrases\n")
            proh_ask = input("")

        # Actual generation
        elif menu_ask == "5":
            for i in range(3):  # appends digits
                for i in range(num_leng_ask):
                    password.append(r.choice(digits))
                for i in range(let_leng_ask):  # Appends letters
                    if case_ask.lower() == "upper" or \
                       case_ask.lower() == "uppercase":
                        password.append(r.choice(alphabets).upper())
                    elif "lower" in case_ask.lower():
                        password.append(r.choice(alphabets).lower())
                if case_ask.lower() == "both":
                    password.append(r.choice(alphabets).upper())
                    password.append(r.choice(alphabets).lower())
                    for i in range(let_leng_ask - 2):
                        password.append(r.choice(alphabets))
                for i in range(sym_leng_ask):  # Appends symbols
                    password.append(r.choice(high_spe_characters))

                # Gets rid of prohibited symbols if there are any
                for i in range(1, len(password)):
                    try:
                        if password[i] in proh_ask:
                            typechar = type_detection(password[i])
                            while password[i] in proh_ask:
                                password[i] = r.choice(typechar)
                    except UnboundLocalError:
                        pass

                # Adds words of interest
                try:
                    int_phrase_count = r.randrange(1, 3)
                    for i in range(int_phrase_count):
                        password.append(int_phrase_ask[r.randrange
                                                       (len(int_phrase_ask))])
                except UnboundLocalError:
                    pass

                r.shuffle(password)

                # Prints password
                print("your password could be ", end="")
                for i in password:
                    print(i, end="")
                print("\n")
                save.append("".join(password))
                time.sleep(0.7)

                password.clear()
                password.append(aska)

            time.sleep(2)
            break

        # Quits
        elif menu_ask == "6" or menu_ask == "quit":
            break

        # Accepts wrong inputs
        else:
            print("that is not a menu option...yet")
            time.sleep(1)
