import random as r
import string
import time

alphabets = list(string.ascii_letters)
digits = list(string.digits)
med_spe_characters = list("!@#$%^&*")
high_spe_characters = list("!@#$%^&*()_-+={[}]|\:;\"\'<,>.?/~`")

menu = ["select desired character types", "set amount of desired characters",
        "provide word of interest", "prohibit characters",
        "generate password", "quit"]


def type_detection(charr):
    if charr in alphabets:
        typpe = alphabets
    elif charr in digits:
        typpe = digits
    else:
        typpe = high_spe_characters
    return typpe


def pw_manipulation(password, save):

    num_leng_ask = 0
    let_leng_ask = 0
    case_ask = "a"
    sym_leng_ask = 0

    checkp_1 = 1
    print("welcome to the advanced settings menu, you can customize your" +
          " password with even\ngreater flexibility in here\n")

    time.sleep(2)

    aska = input("what is your key phrase? if none press enter. " +
                 "Please ensure this phrase does not\nexist in your " +
                 "username\n")

    if aska == "\n":
        aska = ""
    password.append(aska)

    time.sleep(1.5)
    print("Please note that the first two options that will be displayed " +
          "are manetory")
    time.sleep(1.5)

    while True:
        print("You can:\n")
        count = 1
        for i in menu:
            print(str(count) + ". " + i)
            count += 1
            print("\t")
        time.sleep(2)
        menu_ask = input("Type 1 for the 1st option, 2 for the 2nd option, " +
                         "and so on, type quit to end the program\n")

        if menu_ask == "1":
            print("you can have:\n\t- numbers\n\t- letters\n\t- symbols\n")
            type_ask = input("which type(s) of characters do you want in " +
                             "your password? type all that apply before " +
                             "pressing enter\n")
            time.sleep(0.5)
            print("Preference(s) noted\n")

        elif menu_ask == "2":
            if "number" in type_ask.lower():
                num_leng_ask = int(input("how many numbers do you want in " +
                                         "your password?\n"))
                time.sleep(0.5)
                print("understood")
            else:
                num_leng_ask = 0

            if "letter" in type_ask.lower():
                let_leng_ask = int(input("how many letters do you want in " +
                                         "your password?\n"))
                time.sleep(0.5)
                while checkp_1 > 0:
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

            if "symbol" in type_ask.lower():
                sym_leng_ask = int(input("how many symbols do you want in " +
                                         "your password?\n"))
                time.sleep(0.5)
                print("ok")

            if "number" not in type_ask.lower() and "letter" not in \
               type_ask.lower() and "symbol" not in type_ask.lower():
                print("You haven't selected your character types yet, " +
                      "please go back and do so\n")

        elif menu_ask == "3":
            print("what are your word(s) of interest? This will assist you " +
                  "in better memorization of the\npassword. Separate by " +
                  "space and press enter when finished\n")
            int_phrase_ask = input("")
            int_phrase_ask = int_phrase_ask.split(" ")

        elif menu_ask == "4":
            print("Type in all the characters you do not want to have in " +
                  "the final product, press enter after you are finished. " +
                  "Note that this will NOT affect your inputted phrases\n")
            proh_ask = input("")

        elif menu_ask == "5":
            for i in range(3):
                for i in range(num_leng_ask):
                    password.append(r.choice(digits))
                for i in range(let_leng_ask):
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
                for i in range(sym_leng_ask):
                    password.append(r.choice(high_spe_characters))

                for i in range(1, len(password)):
                    try:
                        if password[i] in proh_ask:
                            typechar = type_detection(password[i])
                            while password[i] in proh_ask:
                                password[i] = r.choice(typechar)
                    except UnboundLocalError:
                        pass

                try:
                    int_phrase_count = r.randrange(1, 3)
                    for i in range(int_phrase_count):
                        password.append(int_phrase_ask[r.randrange
                                                       (len(int_phrase_ask))])
                except UnboundLocalError:
                    pass

                r.shuffle(password)

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

        elif menu_ask == "6" or menu_ask == "quit":
            break

        else:
            print("that is not a menu option...yet")
            time.sleep(1)
