def encode(string):
    # after is the encoded string
    after = ''
    for digit in string:
        # add 3 to digit and take mod 10
        after += str((int(digit) + 3) % 10)
    return after


def decode(string):
    before = ''
    for digit in string:
        # subtract 3 from each digit and handle underflow by adding 10 before taking mod 10
        before += str((int(digit) - 3 + 10) % 10)
    return before


if __name__ == '__main__':
    # current stored password
    current_pwd = None
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        # get option
        option = int(input("Please enter an option: "))
        if option == 3:
            # exit
            break
        elif option == 1:
            # ask for and store the password
            pwd = input("Please enter your password to encode: ")
            current_pwd = encode(pwd)
            print("Your password has been encoded and stored!")
        elif option == 2:
            # display the decoded password
            print(f"The encoded password is {current_pwd}, and the original password is {decode(current_pwd)}")
        print()