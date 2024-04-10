def decode(encode_pass):
    new_pass = []
    for num in encode_pass:
        int_num = int(num)
        int_num -= 3
        str_num = str(int_num)
        new_pass.append(str_num)
    decode_pass = ''.join(new_pass)
    return decode_pass

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
            new_pass = decode(final_encode)
            print(f'The encoded password is {final_encode}, and the original password is {new_pass}.\n')

        if menu_option == 3:
            break

if __name__ == "__main__":
    main()