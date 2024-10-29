import random
import string


def generatePassword(miniLength, number = True, specialCharaters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    
    if number:
        characters += digits
        
    if specialCharaters:
        characters += special
    
    pwd = ''
    meetCriteria = False
    hasNumber = False
    hasSpecial = False
    
    while not meetCriteria or len(pwd) < miniLength:
        newChar = random.choice(characters)
        pwd += newChar
        
        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True
        
        
        meetCriteria = True
        if number:
            meetCriteria = hasNumber
        if specialCharaters:
            meetCriteria = meetCriteria and hasSpecial 
            
    return pwd


miniLength = int(input('Enter the minimum length: '))
hasNumber = input('Do you want numbers (y/n)? ').lower() == 'y'
hasSpecial = input('Do you want special character (y/n)? ').lower() == 'y'


pwd = generatePassword(miniLength, hasNumber, hasSpecial)
print(pwd) 