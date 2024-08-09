def encrypt(text,s):
 result = ""
 for i in range(len(text)):
  char=text[i]
  if(char.isupper()):
   result += chr(((ord(char)-65)*s)%26+65)
  else:
   result += chr(((ord(char)-97)*s)%26+97)
 return result

def decrypt(text,s):
 result = ""
 for i in range(len(text)):
  char=text[i]
  if(char.isupper()):
   result += chr(((ord(char)-65)* pow(s,-1,26))%26+65)
  else:
   result += chr(((ord(char)-97)* pow(s,-1,26))%26+97)
 return result

text = input("Input : ")  
shift = int(input("Shift pattern : "))
choice = int(input("Encrypyt(1)/Decrypt(2)?"))
if choice==1:
 print("Cipher: " + encrypt(text, shift))
elif choice==2:
 print("Decrypted text: " + decrypt(text, shift))
else: 
 print("Invalid") 
