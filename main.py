import string
import random as r
import time
import PwGenProcess as PGen
import AdvancedPwSett as APS
import PwSave

alphabets = list(string.ascii_letters)

type_count = ["num", "let", "sym"]
password = []
final_pw_list = []

checkp_1 = 1
checkp_2 = 1

while True:
    print("welcome to password generator. This is a place for you to " +
          "develop a satisfactory password with great levels of " +
          "customization. \ntype anything to start, and type quit to " +
          "stop the program\n")
    touch = input()
    if touch == "quit":
        break

    time.sleep(1)

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

    while checkp_1 == 1:
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
                                 "convenience\n"))

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

    if security_lvl == "quit":
        break

    time.sleep(0.5)
    print("generating...")
    time.sleep(1)

    password.append(must_phrase)

    for i in range(3):
        result = PGen.GenPro(p_length, must_phrase, type_count, password)

        if security_lvl.lower() == "low":
            result.low_secur()

        elif security_lvl.lower() == "med" or security_lvl.lower() == "medium":
            result.med_secur()

        elif security_lvl.lower() == "high":
            result.high_secur()

        elif "recom" in security_lvl.lower():
            result.common_website_requirements()

        r.shuffle(result.password)
        print("".join(result.password) + " could be your password")
        time.sleep(0.7)

        final_pw_list.append("".join(result.password))
        password.clear()
        password.append(must_phrase)

    time.sleep(1)

    checkp_2 = 1

    while True:
        cont_ask = input("do you want to generate more password? type quit " +
                         "to stop the program, continue to use again, " +
                         "advanced to access the advanced generator, or save" +
                         " to save the generated passwords\n")

        if "quit" in cont_ask.lower():
            break
        elif "cont" in cont_ask.lower():
            break
        elif "adv" in cont_ask.lower():
            time.sleep(1)
            password.clear()
            APS.pw_manipulation(password, final_pw_list)
        elif "sav" in cont_ask.lower():
            PwSave.file_save(final_pw_list)
        else:
            print("invalid input!")

    if "quit" in cont_ask.lower():
        break
    elif "cont" in cont_ask.lower():
        continue
