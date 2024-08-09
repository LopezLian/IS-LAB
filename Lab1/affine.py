def encrypt(text,a,b):
 result = ""
 for i in range(len(text)):
  char=text[i]
  if(char.isupper()):
   result += chr((((ord(char)-65)*a)+b)%26+65)
  else:
   result += chr((((ord(char)-97)*a)+b)%26+97)
 return result

def decrypt(text,a,b):
 result = ""
 for i in range(len(text)):
  char=text[i]
  if(char.isupper()):
   result += chr((((ord(char)-65)-b)*pow(a,-1,26))%26+65)
  else:
   result += chr((((ord(char)-97)-b)*pow(a,-1,26))%26+97)
 return result

text = input("Input text : ")  
a = int(input("a : "))
b = int(input("b : "))
choice = int(input("Encrypyt(1)/Decrypt(2)?"))
if choice==1:
 print("Cipher: " + encrypt(text,a,b))
elif choice==2:
 print("Decrypted text: " + decrypt(text,a,b))
else: 
 print("Invalid")  
