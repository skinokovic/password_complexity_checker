
import re  #this module provides regular expression supports


def check_password_strength(password):
    length_limit = len(password) >= 8 #length must be greater or equal to 8abc
    lowercase_check = re.search(r'[a-z]',password) is not None #check for the presence of lowercase letters
    uppercase_check = re.search(r'[A-Z]', password) is not None #check for the presence of uppercase letters
    number_check = re.search(r'\d', password) is not None #check for the presence of numbers
    special_character_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None #check for the presence of special characters

#variable to hold result of the check
    check_if_criteria_is_met = sum([length_limit, lowercase_check, uppercase_check, number_check, special_character_check])
    if check_if_criteria_is_met == 5:
        return "Strong Password"
    elif 3 <= check_if_criteria_is_met < 5:
        return "Moderate Password"
    else:
        return "Weak Password"
#Print("*** Password Complexity Checker Program ***")
password = input("Enter password to check its strength:")#Enter your preferred password
strength = check_password_strength(password) #check for password complexity using the check_password_strength function
print(f"Password Strength: {strength}")#output the result




