alphebet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_number):
    cipher_text = ""

    for x in original_text:
        shifted_position = alphebet.index(x) + shift_number
        cipher_text += alphebet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")




encrypt(text, shift)

