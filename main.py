import random
import string

def generate_password(length=12, use_digits=True, use_uppercase=True, use_lowercase=True, use_symbols=True):
    character_pool = ""
    if use_digits:
        character_pool += string.digits
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected")
    
    return "".join(random.choice(character_pool) for _ in range(length))

def generate_multiple_passwords(count=5, length=12, **kwargs):
    return [generate_password(length, **kwargs) for _ in range(count)]

def save_passwords_to_file(passwords, filename="passwords.txt"):
    with open(filename, "w") as file:
        for pwd in passwords:
            file.write(pwd + "\n")
    print(f"Passwords saved to {filename}")

if __name__ == "__main__":
    count = int(input("Enter number of passwords to generate: "))
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
    
    passwords = generate_multiple_passwords(count, length, use_digits=use_digits, use_uppercase=use_uppercase, use_lowercase=use_lowercase, use_symbols=use_symbols)
    for pwd in passwords:
        print(pwd)
    
    save_option = input("Save passwords to file? (y/n): ").strip().lower()
    if save_option == "y":
        save_passwords_to_file(passwords)
