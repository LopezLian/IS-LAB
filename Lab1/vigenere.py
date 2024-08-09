def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
        return "".join(key)

def encrypt(text, key):
    result = ""
    key = generate_key(text, key)  
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
           
            result += chr((ord(char) + ord(key[i]) - 2 * 65) % 26 + 65)
        elif char.islower():
          
            result += chr((ord(char) + ord(key[i]) - 2 * 97) % 26 + 97)
        else:
            
            result += char
    return result

def decrypt(text, key):
    result = ""
    key = generate_key(text, key)  
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            
            result += chr((ord(char) - ord(key[i]) + 26) % 26 + 65)
        elif char.islower():
           
            result += chr((ord(char) - ord(key[i]) + 26) % 26 + 97)
        else:
           
            result += char
    return result


a = input("TEXT: ")
b = input("KEYWORD: ")
choice = int(input("ENCRYPT(1)/DECRYPT(2)? "))

if choice == 1:
    print("Encrypted text:", encrypt(a, b))
elif choice == 2:
    print("Decrypted text:", decrypt(a, b))
else:
    print("Enter a valid choice (1 or 2)")

