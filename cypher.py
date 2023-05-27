user_message = input("Input text: ")    # promt user for input
encrypted_characters = []               # create empty list for cypher function

def cypher(user_message):               # create cypher function
    character_num = []                  # create empty lists to append new values to
    encrypted_characters = []

    for c in user_message:
        if c.isupper():                 # iterate through capital values
            character_num.append(ord(c) + 15)   # convert to acsii value + 15
            for i in range(len(character_num)): 
                if character_num[i] > 90:       # subtract 26 if acsii value exceeds Z value 
                    character_num[i] = character_num[i] - 26 # to give cyclical value
                    
            encrypted_characters.append(chr(character_num[i]))
                                                    # convert new value to letter and append to
        elif c.islower():                           # encrypted_characters list
            character_num.append(ord(c) + 15)
            for i in range(len(character_num)):     # repeat for lowercase characters
                if character_num[i] > 122:
                    character_num[i] = character_num[i] - 26
                    
            encrypted_characters.append(chr(character_num[i]))
        
        else: encrypted_characters.append(c)        # values that aren't letters are not encrypted
                                                    # directly append to encrypted_characters
                
    return(encrypted_characters)

encrypted_message = ''.join(cypher(user_message))   # convert the list to a string

print(encrypted_message)