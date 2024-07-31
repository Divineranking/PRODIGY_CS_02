import re

def assess_password_strength(password):
   
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    
    if not re.search(r'[0-9]', password):
        return "Password should contain at least one digit."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character."
    
    return "Password is strong."

def main():
    while True:
        password = input("Enter a password to assess its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye!")
            break
        
        strength_message = assess_password_strength(password)
        print(strength_message)

if __name__ == "__main__":
    main()
