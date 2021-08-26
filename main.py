# Encryption/Decryption Algorithm using Keys #
# Developed by Nathan Clark #


def encrypt_text():
    print("-----Encrypt Function-----")
    print("Enter the encryption key:")
    user_key: str = input()
    print("Enter text to encrypt:")
    user_text: str = input()

    i = 0
    new_output = ""
    for i in range(0, len(user_text)):
        mod = i % len(user_key)
        num = ((ord(user_key[mod]) + ord(user_text[i])) % 122)

        if num < 32:
            new_output += chr(((ord(user_key[mod]) + ord(user_text[i])) % 122) + 32)
        else:
            new_output += chr((ord(user_key[mod]) + ord(user_text[i])) % 122)

        i += 1

    print("-----Encrypted Text Below-----")
    print(new_output)

    display_choices()
    choice_prompt()


def decrypt_text():
    print("-----Decrypt Function-----")
    print("Enter the decryption key:")
    user_key: str = input()
    print("Enter text to decrypt:")
    user_text: str = input()

    i = 0
    new_output = ""
    for i in range(0, len(user_text)):
        mod = i % len(user_key)
        #print(ord(user_text[i]))
        premod_num = 122 + ord(user_text[i])
        #print(premod_num)

        enc_num = premod_num - ord(user_key[mod])
        if enc_num == 64:
            enc_num = 32
        #print(enc_num)
        new_output += chr(enc_num)

    print(new_output)


def display_choices():
    print("\nPress 1 to encrypt")
    print("Press 2 to decrypt")
    print("Press 3 to exit")


def choice_prompt():
    is_running = True

    while is_running:
        choice = input()

        if choice == '1':
            encrypt_text()
        elif choice == '2':
            decrypt_text()
        elif choice == '3':
            is_running = False
            print("Program closing....")
            exit()
        else:
            print("Invalid Input. Try Again")


if __name__ == "__main__":
    display_choices()
    choice_prompt()
