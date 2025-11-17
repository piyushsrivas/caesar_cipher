def encrypt(message, shift):
    result = ""
    
    for char in message:
        if char.isalpha():  
            shift_amount = shift % 26  
            if char.isupper():
                result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            result += char  
    return result


def decrypt(message, shift):
    return encrypt(message, -shift)


# -------- Main Program ----------
print("----- Caesar Cipher Program -----")
text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\nEncrypted Message:", encrypted_text)
print("Decrypted Message:", decrypted_text)
