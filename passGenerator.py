import random
import string

def passLength():
    while True:
        try:
            length = int(input("Enter desired length for password [minimum 8] : "))
            if length >= 8:
                return length
            else:
                print("Password must have atleast 8 characters.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def characterPreferences():
    include_letters = False
    include_numbers = False
    include_symbols = False

    character_chosen = ""

    while not(include_letters or include_numbers or include_symbols):
        include_letters = input("Include letters (y/n)? ").lower() == 'y'
        include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
        include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

        if not(include_letters or include_numbers or include_symbols):
            print("Atleast one character type must be chosen(letters, numbers or symbols).")
    
    
    if include_letters:
        character_chosen += string.ascii_letters
    if include_numbers:
        character_chosen += string.digits
    if include_symbols:
        character_chosen += string.punctuation

    return character_chosen
        
def generatePassword(length, char_chosen):
    password = "".join(random.choice(char_chosen) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    password_length = passLength()
    
    characters_chosen = characterPreferences()
    
    final_password = generatePassword(password_length, characters_chosen)
    
    print(f"Your generated password🔒 is: {final_password}")
    

if __name__ == "__main__":
    main()