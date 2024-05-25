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
        

    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        end_of_game = False
        restart = input("Do you want to restart the cipher program? Yes or No:\n").lower()
        
