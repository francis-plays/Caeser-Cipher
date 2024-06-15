letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)
#This block is creating the encryption function
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index <0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext


#this block prints out the header for the caeser cipher program
print()
print('Caeser Cipher program V.1'.upper())
print()

# This block asks or prompts the user if the user wants to encrypt or decrypt the cipher
print('Do you want to encrypt or decrypt')
user_input = input('e/d:').lower()

if user_input == 'e':
    print('Encryption mode selected'.upper())
    print()
    key = int(input("Enter the key(1 through 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == "d":
    print('Decryption mode selected'.upper())
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
