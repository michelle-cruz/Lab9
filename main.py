def main():
    while True:
        print("Menu")
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        menu_option = input('Please enter an option: ')
        if menu_option.isdigit():
            menu_option = int(menu_option)

        if menu_option == 1:
            password = input('Please enter your password to encode: ')
            encode = []
            for i in range(len(password)):
                new_digit = int(password[i]) + 3
                encode.append(str(new_digit))

            final_encode = ''.join(encode)
            print('Your password has been encoded and stored!\n')

        if menu_option == 2:
            print(f'The encoded password is {final_encode}, and the original password is {password}.\n')

        if menu_option == 3:
            break

if __name__ == "__main__":
    main()