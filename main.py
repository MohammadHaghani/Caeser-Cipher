alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar_cipher(text, shift, direction):
	encoded_text = ""
	for char in text:
		if char.isalpha():
			if direction == "encode":
				index = alphabet.index(char)
				encoded_text += alphabet[(index + shift) % 26]
			elif direction == "decode":
				index = alphabet.index(char)
				encoded_text += alphabet[(index - shift) % 26]
		else:
			encoded_text += char
	return encoded_text

result = caesar_cipher(text, shift, direction)
print(f"The {direction}d text is: {result}")


