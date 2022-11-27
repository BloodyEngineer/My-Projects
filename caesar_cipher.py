alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(plain_text, shift_amount, direct):
    cipher_text = ""
    if direct == "decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        position = alphabet.index(letter)
        new_pos = position + shift_amount
        if new_pos >= len(alphabet):
            new_pos -= len(alphabet)
        cipher_text += alphabet[new_pos]
    print(f"The {direct}d text is {cipher_text}")
from art_caesar_cipher import logo
print(logo)
end_message = False
while end_message is False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print("Ended.")
        end_message = True
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    caesar(plain_text = text, shift_amount=shift, direct=direction)
    again = input("Do you want to go again? Type 'yes' or 'no' ").lower()
    if again == "no":
        print("Caesar Cipher now ended.")
        end_message = True
