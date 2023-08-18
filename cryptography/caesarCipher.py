import time

def decodeCaesarCipher(shift, text):
    text = text.lower()
    message = ""

    for char in text:
        anscii = ord(char) - shift
        if (anscii > 122):
            message += chr(anscii - 25)
        elif (anscii < 97):
            message += chr(anscii + 25)
        else:
            message += chr(anscii)

    return message

def encodeCaesarCipher(shift, text):
    text = text.replace(" ", "").lower()
    message = ""

    for char in text:
        anscii = ord(char) + shift
        if (anscii > 122):
            message += chr(anscii - 25)
        elif (anscii < 97):
            message += chr(anscii + 25)
        else:
            message += chr(anscii)

    return message

print(encodeCaesarCipher(3, "hello world"))
print(decodeCaesarCipher(3, encodeCaesarCipher(3, "hello world")))

# for i in range(0, 26):
#     print(encodeCaesarCipher(i, "Hello world") + "\n")
#     time.sleep(3)