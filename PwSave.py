# importing required modules
import time


"""This is the function that saves the password"""


def file_save(password):

    # setting up required variables
    count = 1
    checkp_1 = 1
    save_p = []
    locat = []

    time.sleep(1)

    # prints all stored passwords
    for i in password:
        print(f"{count} - {i}")
        count += 1

    time.sleep(1)

    # checkpoint system to accept wrong inputs
    # asks which passwords the users wants to save
    while checkp_1 != 0:
        num_ask = input("which of the following do you want to save? input " +
                        "the number in front of the password. \nSeparate by " +
                        "space and enter all before pressing enter\n")
        num_ask = num_ask.split(" ")

        # handles error
        for i in num_ask:
            try:
                if int(i) > len(password):
                    print("one or more of the index you chose was out of " +
                          "range, please try again\n")
                    break
            except ValueError:
                print("you did not input a number!\n")
                break

        # handles error
        try:
            if int(i) <= len(password):
                checkp_1 -= 1
            else:
                continue
        except ValueError:
            continue

    time.sleep(1)

    # asks what purpose each pw serves to better create the saved file
    for i in num_ask:
        if int(i) <= len(password):
            save_p.append(password[int(i) - 1])
            locat_ask = input("what account or destination is " +
                              f"{password[int(i) - 1]} for?\n\t - ")
            locat.append(locat_ask)

    f = open("generated password.txt", "w+")  # creates a .txt file

    # writes the pws and their purposes in an organized manner in file
    for i in range(len(num_ask)):
        f.write("\t- the password for " + locat[i] + " is " +
                save_p[i])
        f.write("\n----------------------------------------------" +
                "-----------------\n")
    print("password(s) successfully saved\n")
