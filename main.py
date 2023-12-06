alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:  # Check if the character is a letter
            position = alphabet.index(char.lower())  # Get the index of the lowercase version of the character
            new_position = (position + shift_amount) % 26  # Calculate the new position using the shifted amount
            end_text += alphabet[new_position] if char.islower() else alphabet[new_position].upper()  # Append the shifted character back to end_text
        else:
            end_text += char  # If the character is not a letter, directly append it to end_text

    print(f"Here's the {cipher_direction}d result: {end_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
end_of_game = False
restart = input("Do you want to restart the cipher program? Yes or No:\n").lower()
while not end_of_game:
    if restart == "no":
        print("Goodbye")
        end_of_game = True
        
        
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        end_of_game = False
        restart = input("Do you want to restart the cipher program? Yes or No:\n").lower()
        