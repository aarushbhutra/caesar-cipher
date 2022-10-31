#Create a function called shifter

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

def shifter():
    #Take input from the user for the amount of shift
    shift = int(input("Enter the amount of shift: "))
    #Take input from the user for the message to be encrypted
    message = input("Enter the message to be encrypted: ")
    #For each letter in the message get its index in the alphabet array and add the shift to it
    #Then get the letter at that index in the alphabet array
    #Print the encrypted message
    encrypted_message = ""
    for letter in message:
        if letter in alphabet:
            encrypted_message += alphabet[(alphabet.index(letter) + shift) % 26]
        elif letter in alphabet_capital:
            encrypted_message += alphabet_capital[(alphabet_capital.index(letter) + shift) % 26]
        elif letter in numbers:
            encrypted_message += numbers[(numbers.index(letter) + shift) % 10]
        else:
            encrypted_message += letter
    print("Encrypted message: " + encrypted_message)

#Create a function called decrypter
def decrypter():
    #Take input from the user for the amount of shift
    shift = int(input("Enter the amount of shift: "))
    #Take input from the user for the message to be encrypted
    message = input("Enter the message to be decrypted: ")
    #For each letter in the message get its index in the alphabet array and subtract the shift from it
    #Then get the letter at that index in the alphabet array
    #Print the encrypted message
    decrypted_message = ""
    for letter in message:
        if letter in alphabet:
            decrypted_message += alphabet[(alphabet.index(letter) - shift) % 26]
        elif letter in alphabet_capital:
            decrypted_message += alphabet_capital[(alphabet_capital.index(letter) - shift) % 26]
        elif letter in numbers:
            decrypted_message += numbers[(numbers.index(letter) - shift) % 10]
        else:
            decrypted_message += letter
    print("Decrypted message: " + decrypted_message)

#Create a function called main
def main():
    #Ask the user if they want to encrypt or decrypt a message
    #If they want to encrypt call the shifter function
    #If they want to decrypt call the decrypter function
    #If they enter anything else print an error message
    choice = input("Do you want to encrypt or decrypt a message? ")
    if choice == "encrypt":
        shifter()
    elif choice == "decrypt":
        decrypter()
    else:
        print("Invalid choice")

#Call the main function
main()
