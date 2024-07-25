import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    characters = []
    characters.append(random.choice(lowercase_letters))
    characters.append(random.choice(uppercase_letters))
    characters.append(random.choice(digits))
    characters.append(random.choice(special_characters))
    all_chars = lowercase_letters + uppercase_letters + digits + special_characters
    password = ''.join(random.choice(all_chars) for _ in range(length) )
    return password
def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a positive integer.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

