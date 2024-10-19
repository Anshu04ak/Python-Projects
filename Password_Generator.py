import random
import string

def generate_password(length):
    """
    Generates a strong password of the given length.
    The password contains a mix of uppercase, lowercase, digits, and special characters.
    """
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    # Define the character sets for the password
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # Special characters like !, @, #

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with a random selection of all characters
    all_chars = lower + upper + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the generated password to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return the password
    return ''.join(password)

if __name__ == "__main__":
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired password length: "))
        
        # Generate the password
        password = generate_password(length)

        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number for the password length.")
