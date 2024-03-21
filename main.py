def displayMenu():
    print('\nMenu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode(password):
    res = ''
    for letter in password:
        res += str(int(letter)+3)
    print('Your password has been encoded and stored!')
    return res


def decode(password):
    decoded_password = ""  # stores the decoded pw


    for digit in password:
        # Convert the digit to a number, subtract 3, handle negative numbers, and ensure it's a single digit
        decoded_digit = (int(digit) - 3 + 10) % 10
        # Add the decoded digit to the decoded password
        decoded_password += str(decoded_digit)

    return decoded_password



def main():
    password = ''
    choice = -1

    while True:
        displayMenu()
        choice = int(input('Please enter an option: '))

        if choice == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)

        if choice == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')

        if choice == 3:
            break

if __name__ == '__main__':
    main()