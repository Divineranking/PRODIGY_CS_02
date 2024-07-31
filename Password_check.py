import re
from colorama import Fore, Style, init

def assess_password_strength(password):
    requirements = []

    if len(password) < 8:
        requirements.append(f"{Fore.RED}Password is too short. It should be at least 8 characters long.{Style.RESET_ALL}")
    
    if not re.search(r'[A-Z]', password):
        requirements.append(f"{Fore.RED}Password should contain at least one uppercase letter.{Style.RESET_ALL}")
    
    if not re.search(r'[a-z]', password):
        requirements.append(f"{Fore.RED}Password should contain at least one lowercase letter.{Style.RESET_ALL}")
    
    if not re.search(r'[0-9]', password):
        requirements.append(f"{Fore.RED}Password should contain at least one digit.{Style.RESET_ALL}")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        requirements.append(f"{Fore.RED}Password should contain at least one special character.{Style.RESET_ALL}")
    
    if not requirements:
        return f"{Fore.GREEN}Password is strong.{Style.RESET_ALL}"
    else:
        return "\n".join(requirements)

def main():
    init(autoreset=True)
    while True:
        password = input("Enter a password to assess its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye!")
            break
        
        strength_message = assess_password_strength(password)
        print(strength_message)

if __name__ == "__main__":
    main()
